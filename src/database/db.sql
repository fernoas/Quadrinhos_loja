CREATE TABLE IF NOT EXISTS produtos(
    code int(4) UNSIGNED ZEROFILL NOT NULL,
    name CHAR(50),
    stock NOT NULL,
    value FLOAT,
    id_category TINYINT NOT NULL,
    PRIMARY KEY('code')
);

CREATE TABLE IF NOT EXISTS produtos(
    id TINYINT not NULL,
    name CHAR(40) NOT NULL,
    description VARCHAR(200),
    PRIMARY KEY('id')
);

ALTER TABLE produtos ADD FOREIGN KEY ('id_category')REFERENCES categories('id');



