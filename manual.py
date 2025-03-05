import libs
import classification
import functions.queries

##Lançamento manual ou nao?
print('\n######## Digite o valor gasto ########\n')
valor_manual = input()

dt_launch = libs.datetime.now()

#Cria um data frame
ticket_lancamento = {
    'fk_id_account': classification.escolha_id_account
    , 'fk_id_transaction_type': classification.escolha_id_transaction_type
    , 'fk_id_subcategory': [classification.escolha_id_sub_category]
    , 'url_nfe': ''
    , 'establishment': ''
    , 'buy_address': ''
    , 'dt_ticket': ''
    , 'dt_launch': dt_launch
}
df_transaction = libs.pd.DataFrame(data=ticket_lancamento)

##insere lancamento
functions.queries.insert_trancao(df_transaction)

##Resgata as accounts registradas em BD
url_cara = functions.queries.get_last_transaction()
fk_id_transaction = url_cara.at[0,'id_transaction']

ticket = libs.pd.DataFrame({'total_value':[valor_manual], "fk_id_transaction":[fk_id_transaction]})
ticket['total_value'] = ticket['total_value'].str.replace(',', '.')

functions.queries.set_ticket(ticket)