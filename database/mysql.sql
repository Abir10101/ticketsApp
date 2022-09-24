DROP TABLE IF EXISTS tickets;
DROP TABLE IF EXISTS branches;

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
