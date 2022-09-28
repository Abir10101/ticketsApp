CREATE TABLE tickets (
    id  SERIAL  NOT NULL,
    t_code  VARCHAR(20)  NOT NULL  UNIQUE,
    t_description  VARCHAR(100)  NOT NULL,
    t_status ENUM( 'pending', 'ongoing', 'done' )  NOT NULL
);

CREATE TABLE branches (
    id  SERIAL  NOT NULL,
    ticket_id  BIGINT  NOT NULL,
    b_name  VARCHAR(20)  NOT NULL  UNIQUE,
    b_status ENUM( 'live', 'not_live' )  NOT NULL
);

CREATE TABLE users (
    id  SERIAL  NOT NULL,
    u_username  VARCHAR(50)  NOT NULL  UNIQUE,
    u_password  VARCHAR(200)  NOT NULL
);

ALTER  TABLE  tickets  ADD  user_id  BIGINT  NOT NULL;
ALTER  TABLE  users  ADD  u_name  VARCHAR(50)  NOT NULL;
ALTER  TABLE  users  ADD  u_secret  VARCHAR(15)  NOT NULL;
