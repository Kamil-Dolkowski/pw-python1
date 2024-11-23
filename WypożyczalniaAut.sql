CREATE DATABASE car_rental;

\c car_rental

CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    phone_number VARCHAR(9) NOT NULL,
    email VARCHAR(100) NOT NULL
);

CREATE TABLE cars (
    car_id SERIAL PRIMARY KEY,
    manufacturer VARCHAR(20) NOT NULL,
    model VARCHAR(20) NOT NULL,
    color VARCHAR(20) NOT NULL,
    reservation_state VARCHAR(20) NOT NULL
);

CREATE TABLE reservations (
    reservation_id SERIAL PRIMARY KEY,
    customer_id SERIAL REFERENCES customers(customer_id),
    car_id SERIAL REFERENCES cars(car_id),
    begin_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL
);

CREATE TABLE payments (
    payment_id SERIAL PRIMARY KEY,
    customer_id SERIAL REFERENCES customers(customer_id),
    reservation_id SERIAL REFERENCES reservations(reservation_id),
    payment_value MONEY NOT NULL,
    date TIMESTAMP NOT NULL
);

CREATE TABLE employees (
    employee_id SERIAL PRIMARY KEY,
    name VARCHAR(20) NOT NULL,
    surname VARCHAR(30) NOT NULL,
    phone_number VARCHAR(9) NOT NULL,
    email VARCHAR(100) NOT NULL,
    job_position VARCHAR(20) NOT NULL
);

CREATE TABLE maintenance (
    maintenance_id SERIAL PRIMARY KEY,
    car_id SERIAL REFERENCES cars(car_id),
    info TEXT NOT NULL,
    begin_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL
);
