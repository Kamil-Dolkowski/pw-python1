INSERT INTO customers (customer_id, name, surname, phone_number, email) VALUES 
(1,'Adam','Kowalski','123456789','adam.kowalski@pw.edu.pl'),
(2,'Maja','Tarnowska','222333444','maja.tarnowska@pw.edu.pl');

INSERT INTO cars (car_id, registration_number, manufacturer, model, color, reservation_state) VALUES 
(1,'WP 12P34','Skoda','Oktavia','srebrny','wypożyczony'),
(2,'GD 23N4L','Opel','Astra','zielony','wypożyczony'),
(3,'GD P09WE','Opel','Corsa','biały','wypożyczony'),
(4,'WPL 09LK','Fiat','Panda','biały','niewypożyczony');

INSERT INTO reservations (reservation_id, customer_id, car_id, begin_date, end_date) VALUES
(1,1,1,'2024-12-12 10:30:00','2025-12-12 12:30:00'),
(2,2,3,'2024-10-12 11:00:00','2025-01-27 16:30:00'),
(3,2,2,'2024-11-20 12:00:00','2026-10-01 17:30:00');

INSERT INTO payments (payment_id,customer_id,reservation_id,payment_value,date) VALUES 
(1,1,1,300.00,'2024-12-10 12:15:00');

INSERT INTO employees (employee_id,name,surname,phone_number,email,job_position) VALUES
(1,'Katarzyna','Nowak','999888777','katarzyna.nowak@pw.edu.pl','sekretarka');

INSERT INTO maintenance (maintenance_id,car_id,info,begin_date,end_date) VALUES 
(1,1,'Wymiana przedniej prawej lampy.','2024-11-15 12:07:34', '2024-11-15 13:02:01'),
(2,1,'Wymiana lewego koła.','2024-10-15 15:31:34', '2024-10-15 16:46:33'),
(3,2,'Wymiana bezpiecznika.','2024-11-20 15:27:34', '2024-11-21 16:46:33'),
(4,1,'Rutynowa kontrola.','2023-11-15 14:22:34', '2023-11-15 16:12:04'),
(5,2,'Wymiana przedniej prawej lampy.','2022-11-15 15:31:34', '2022-11-15 16:32:33');
