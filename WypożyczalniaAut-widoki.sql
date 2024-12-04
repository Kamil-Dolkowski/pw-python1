CREATE VIEW last_3_maintenances AS
SELECT c.manufacturer, c.model, m.info, m.begin_date, m.end_date 
FROM maintenance m
JOIN cars c ON (m.car_id = c.car_id)
ORDER BY end_date DESC
LIMIT 3;

CREATE VIEW opel_cars AS
SELECT registration_number,manufacturer,model,color,reservation_state 
FROM cars 
WHERE manufacturer = 'Opel';

CREATE VIEW number_of_reserved_cars AS
SELECT c.name, c.surname, COUNT(r.customer_id) AS reserved_cars
FROM reservations r
JOIN customers c ON (r.customer_id = c.customer_id)
GROUP BY r.customer_id,c.name,c.surname;