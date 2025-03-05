CREATE TABLE IF NOT EXISTS category(
	id_category INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(100),
    situation VARCHAR(2),
    date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS subcategory(
	id_subcategory INT AUTO_INCREMENT PRIMARY KEY,
    subcategory_name VARCHAR(100),
    fk_id_category INT,
    FOREIGN KEY (fk_id_category) REFERENCES category(id_category),
	date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS account(
	id_account INT AUTO_INCREMENT PRIMARY KEY,
    account_name VARCHAR(255),
    situation VARCHAR(2),
	date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transaction_type(
	id_transaction_type INT AUTO_INCREMENT PRIMARY KEY,
    transaction_type_name VARCHAR(255),
    situation VARCHAR(2),
	date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS transaction(
	  id_transaction INT AUTO_INCREMENT PRIMARY KEY
    , url_nfe LONGTEXT
    , establishment VARCHAR(255)
    , buy_address longtext
    , dt_ticket datetime(6)
    , dt_launch datetime(6)
    , situation VARCHAR(2)
    , fk_id_account int(11)
    , fk_id_subcategory int(11)
    , fk_id_transaction_type int(11)
    /*, FOREIGN KEY (fk_id_account) REFERENCES account(id_account)
    , FOREIGN KEY (fk_id_subcategory) REFERENCES subcategory(id_subcategory)
    , FOREIGN KEY (fk_id_transaction_type) REFERENCES transaction_type(id_transaction_type)*/
	, date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    , date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS ticket(
	  id_ticket INT AUTO_INCREMENT PRIMARY KEY
	, cod_product int(11)
    , purchased_item varchar(155)
    , quantity decimal(5,2)
    , measure varchar(15)
    , price decimal(15,2)
    , total_value decimal(15,2)
    , fk_id_transaction int(11)
    , FOREIGN KEY (fk_id_transaction) REFERENCES transaction(id_transaction)
	, date_up TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    , date_down TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- drop database alfred_db