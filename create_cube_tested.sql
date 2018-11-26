select * from pg_table_def;
CREATE TABLE seller_type
(
    id integer primary key identity,
    name varchar(120)
)
CREATE TABLE seller
(
    id integer primary key identity,
    name varchar(120),
    date_born date,
    gender varchar(1),
    dni varchar(20),
    points integer not null,
    seller_type_id integer not null,
    foreign key(seller_type_id) references seller_type(id)
)
CREATE TABLE customer
(
    id integer primary key identity,
    name varchar(120),
    date_born date,
    gender varchar(1),
    dni varchar(20)
)
CREATE TABLE date
(
    id integer primary key identity,
    period integer not null,
    week integer not null
)
CREATE TABLE sale_type
(
    id integer primary key identity,
    name varchar(20)
)
CREATE TABLE product
(
    id integer primary key identity,
    name varchar(120),
    create_date date,
    price real
)
CREATE TABLE sale_product
(
    id integer primary key identity,
    sale_id integer not null,
    product_id integer not null,
    foreign key(product_id) references product(id)
)

CREATE TABLE sale
(
    id integer primary key identity,
    price real,
    date_id integer not null,
    sale_product_id integer not null,
    seller_type_id integer not null,
    seller_id integer not null,
    customer_id integer not null,
    sale_type_id integer not null,
    foreign key(date_id) references DATE(id),
    foreign key(sale_product_id) references sale_product(id),
    foreign key(seller_type_id) references seller_type(id),
    foreign key(seller_id) references seller(id),
    foreign key(customer_id) references customer(id),
    foreign key(sale_type_id) references sale_type(id)
)