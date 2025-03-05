import libs
import functions.queries

##Lançamento manual ou nao?
print('\n######## Seu lançamento será manual ou com link NFE? ########\n')
print('######## Digite M para MANUAL e N para nota fiscal eletrônica ########\n')
type_launch = input()

##Nota PR ou SC?
print('\n######## A NFE é PR ou SC? ########\n')
print('1 - Paraná\n')
print('2 - Santa Catarina\n')
estado_lancamento = input()

##Resgata as accounts registradas em BD
print('\n######## ESCOLHA DE QUAL account QUE SAIRÁ O SEU DINHEIRO ########\n')
df_accounts = functions.queries.get_accounts()
print(df_accounts['account_name'])

id_account = input("\n\nEscolha o ID tipo da account: ")
id_account = libs.pd.to_numeric(id_account)
escolha_nome_transaction = df_accounts.loc[id_account, 'account_name']
escolha_id_account = df_accounts.loc[id_account, 'id_account']
print('\n --> account escolhida: \n' + str(escolha_nome_transaction) + '\n\n')


##Resgata as accounts registradas em BD
print('######## ESCOLHA DO TIPO DE TRANSAÇÃO ########\n')
df_transaction_type = functions.queries.get_transaction_type()
print(df_transaction_type['transaction_type_name'])

id_transaction_type = input("\n\nEscolha o ID tipo de transação: ")
id_transaction_type = libs.pd.to_numeric(id_transaction_type)
escolha_nome_transaction_type = df_transaction_type.loc[id_transaction_type, 'transaction_type_name']
escolha_id_transaction_type = df_transaction_type.loc[id_transaction_type, 'id_transaction_type']
print('\n --> account escolhida: \n' + str(escolha_nome_transaction_type) + '\n\n')


##Resgata as categoryS registradas em BD
print('######## ESCOLHA DA category ########\n')
df_category = functions.queries.get_category()
print(df_category['category_name'])

id_category = input("\n\nEscolha o ID da category: ")
id_category = libs.pd.to_numeric(id_category)
escolha_category_name = df_category.loc[id_category, 'category_name']
escolha_id_category = df_category.loc[id_category, 'id_category']
print('\n --> category escolhida: \n' + str(escolha_category_name) + '\n\n')


##Resgata as SUB-categoryS registradas em BD
print('######## ECOLHA A SUB-category ########\n')
df_sub_category = functions.queries.get_subcategory(escolha_id_category)
print(df_sub_category['subcategory_name'])

id_sub_category = input("\n\nEscolha o ID da Subcategory: ")
id_sub_category = libs.pd.to_numeric(id_sub_category)
escolha_category_name = df_sub_category.loc[id_sub_category, 'subcategory_name']
escolha_id_sub_category = df_sub_category.loc[id_sub_category, 'id_subcategory']
print('\n --> category escolhida: \n' + str(escolha_category_name) + '\n\n')