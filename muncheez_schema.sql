CREATE TABLE users (
    user_id INT NOT NULL AUTO_INCREMENT,
    userName VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    firstName VARCHAR(255) NOT NULL,
    lastName VARCHAR(255) NOT NULL,
    user_address varchar(255) NOT null,
    user_city varchar(255) not null,
    user_state varchar(2) not null,   
    zip_code varchar(5) not null,
    user_email VARCHAR(255) NOT NULL,
    user_phone_number VARCHAR(255) NOT NULL,
    PRIMARY KEY(user_id)
);