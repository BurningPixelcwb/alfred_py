import libs
db_connection_str = 'mysql+pymysql://root:@localhost:3306/alfred_db'
db_connection = libs.create_engine(db_connection_str)

def get_accounts():
    query = "SELECT id_account, account_name FROM account WHERE situation = 'A';"
    df_accounts = libs.pd.read_sql(query, con=db_connection)

    return df_accounts#.to_string(index=False)

def get_transaction_type():
    query = "SELECT id_transaction_type, transaction_type_name FROM transaction_type;"
    df_transaction_type = libs.pd.read_sql(query, con=db_connection)

    return df_transaction_type

def get_category():
    query = "SELECT id_category, category_name FROM category;"
    df_category = libs.pd.read_sql(query, con=db_connection)

    return df_category

def get_subcategory(category):
    query = "SELECT id_subcategory, subcategory_name FROM `subcategory` WHERE fk_id_category = " + str(category) + ";"
    df_sub_category = libs.pd.read_sql(query, con=db_connection)

    return df_sub_category

def insert_trancao(df_transaction):
    df_transaction.to_sql('transaction', db_connection, if_exists='append', index = False)

    return True

def get_last_transaction():
    query = "SELECT * FROM transaction ORDER BY id_transaction DESC LIMIT 1;"
    url_cara = libs.pd.read_sql(query, con=db_connection)

    return url_cara

def set_ticket(ticket):
    ticket.to_sql('ticket', db_connection, if_exists='append', index = False)

    return True