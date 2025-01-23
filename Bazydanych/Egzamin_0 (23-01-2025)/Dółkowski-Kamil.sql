-- Kamil Dółkowski 334531


-- 1

CREATE DATABASE hotel_management;

-- \c hotel_management


-- 2

CREATE SCHEMA views_schema;
CREATE SCHEMA procedures_schema;


-- 3

CREATE USER order_user;
CREATE USER stats_user;

-- Nadawanie uprawnień do ról w punkcie 9


-- 4

CREATE TABLE guests (
    guest_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone_number VARCHAR(12) UNIQUE NOT NULL,
    add_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE rooms (
    room_id SERIAL PRIMARY KEY,
    number INT NOT NULL,
    type VARCHAR(10) NOT NULL,
    price NUMERIC NOT NULL CHECK(price > 0),
    status BOOLEAN NOT NULL DEFAULT TRUE
);


CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    guest_id INT NOT NULL REFERENCES guests(guest_id),
    room_id INT NOT NULL REFERENCES rooms(room_id),
    in_date DATE NOT NULL,
    out_date DATE NOT NULL,
    total_cost NUMERIC NOT NULL,
    reservation_datetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CHECK (out_date > in_date)
);


-- 5

CREATE OR REPLACE VIEW views_schema.available_rooms  AS
SELECT room_id, number, type, price 
FROM rooms
WHERE status = TRUE;


CREATE OR REPLACE VIEW views_schema.reservation_details AS
SELECT res.reservation_id, g.name || ' ' || g.surname AS name_surname, r.number, res.in_date, res.out_date, res.total_cost
FROM reservations res
JOIN guests g ON g.guest_id = res.guest_id
JOIN rooms r ON r.room_id = res.room_id;


CREATE MATERIALIZED VIEW views_schema.room_type_statistics AS
SELECT type, AVG(price) AS avg_price
FROM rooms
GROUP BY type
WITH DATA;


-- 6

CREATE OR REPLACE FUNCTION procedures_schema.calculate_reservation_cost(f_room_id INT, f_in_date DATE, f_out_date DATE)
RETURNS NUMERIC AS $$
DECLARE
    f_price NUMERIC;
BEGIN
    SELECT price FROM rooms WHERE room_id = f_room_id INTO f_price;

    RETURN f_price * (f_out_date - f_in_date);
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE PROCEDURE procedures_schema.create_reservation(p_guest_id INT, p_room_id INT, p_in_date DATE, p_out_date DATE)
LANGUAGE plpgsql AS $$
DECLARE
    p_total_cost NUMERIC;
BEGIN
    IF p_room_id IN (SELECT room_id FROM views_schema.available_rooms WHERE room_id = p_room_id) THEN
        SELECT * FROM procedures_schema.calculate_reservation_cost(p_room_id, p_in_date, p_out_date) INTO p_total_cost;

        INSERT INTO reservations (guest_id, room_id, in_date, out_date, total_cost, reservation_datetime) 
        VALUES (p_guest_id, p_room_id, p_in_date, p_out_date, p_total_cost, CURRENT_TIMESTAMP);

        UPDATE rooms
        SET status = FALSE
        WHERE room_id = p_room_id;
    END IF;
END;
$$;


-- 7

CREATE INDEX guests_idx ON guests(email);

CREATE INDEX rooms_idx ON rooms(type);

CREATE INDEX reservations_in_date_idx ON reservations(in_date);
CREATE INDEX reservations_out_date_idx ON reservations(out_date);


-- 8

CREATE OR REPLACE FUNCTION room_status_change()
RETURNS TRIGGER AS $$
BEGIN
    UPDATE rooms
    SET status = TRUE
    WHERE room_id = OLD.room_id;

    RETURN NULL;
END;
$$ LANGUAGE plpgsql;


CREATE OR REPLACE TRIGGER reservation_trigger
AFTER DELETE
ON reservations
FOR EACH ROW
EXECUTE FUNCTION room_status_change();


-- 9

-- Nadanie uprawnień rolom: order_user i stats_user

GRANT EXECUTE ON PROCEDURE procedures_schema.create_reservation TO order_user;
GRANT SELECT ON views_schema.available_rooms TO order_user;

GRANT SELECT ON views_schema.room_type_statistics TO stats_user;


-- Dane 

INSERT INTO guests (name, surname, email, phone_number) VALUES 
('Kamil', 'Dółkowski', 'kamil.dolkowski@pw.edu.pl', '123456789'),
('Mateusz', 'Nowak', 'mateusz.nowak@onet.pl', '111222333'),
('Oliwia', 'Trzmiel', 'oliwia.trzmiel@pw.edu.pl', '100100100'),
('Wojciech', 'Ignaczak', 'wojciech.ignaczak@pw.edu.pl', '000999888');

INSERT INTO rooms (number, type, price) VALUES
(1, 'Single', 40),
(2, 'Single', 50),
(3, 'Double', 80),
(4, 'Suite', 110);

-- INSERT INTO reservations (guest_id, room_id, in_date, out_date, total_cost) VALUES
-- (1, 1, '2000-01-01', '2000-01-10', 100);

CALL procedures_schema.create_reservation(1, 2, '2020-02-02', '2020-02-12');
CALL procedures_schema.create_reservation(2, 3, '2020-01-01', '2020-01-10');


-- Widoki (5)

SELECT * FROM views_schema.available_rooms;

SELECT * FROM views_schema.reservation_details;

REFRESH MATERIALIZED VIEW views_schema.room_type_statistics;

SELECT * FROM views_schema.room_type_statistics;


-- Procedury (6)

SELECT * FROM procedures_schema.calculate_reservation_cost(1,'2000-01-01','2000-01-11');

CALL procedures_schema.create_reservation(2, 2, '2020-02-02', '2020-02-12');


-- Trigger (8)

DELETE FROM reservations
WHERE reservation_id = 1;


-- SELECT tables

SELECT * FROM guests;

SELECT * FROM rooms;

SELECT * FROM reservations;

