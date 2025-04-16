/*
id, filename, r, g, b
*/

DROP TABLE IF EXISTS files_rgb;

CREATE TABLE IF NOT EXISTS files_rgb (
    id INTEGER PRIMARY KEY,
    filename TEXT NOT NULL,
    r INTEGER checked(0, 255) NOT NULL,
    g INTEGER checked(0, 255) NOT NULL,
    b INTEGER checked(0, 255) NOT NULL
);