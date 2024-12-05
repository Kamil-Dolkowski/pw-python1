CREATE TABLE account (
    account_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL CHECK( LENGTH(password) >= 8 )
    CHECK (first_name !~ '\s' AND last_name !~ '\s'),
    CHECK (email ~* '^\w+@\w+[.]\w+$'),
    CHECK (char_length(password) >= 8)
);