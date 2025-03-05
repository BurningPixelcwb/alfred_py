import libs
import functions.queries
import classification

# INSERE A URL DA NOTA FISCAL
print('######## AGORA QUE ESTÁ TUDO CERTO, BASTA COLAR O LINK DO TICKET! ########\n')
print('Insira a URL da nota fiscal eletronica:')
url_nfe = input()
nav = libs.webdriver.Chrome(service=libs.service)

##Pandas
##Series para lista de compra
df_cod_product = libs.pd.Series([])
df_purchased_item = libs.pd.Series([])
df_quantity = libs.pd.Series([])
df_measure = libs.pd.Series([])
df_price = libs.pd.Series([])
df_total_value = libs.pd.Series([])

#Series para: Local da compra
df_local_compra = libs.pd.Series([])

#Series para: Consumidor

#Series para: Info Gerais

transaction = libs.pd.DataFrame()

ticket = libs.pd.DataFrame()

nav.get(url_nfe)

dt_ticket = nav.find_elements(libs.By.XPATH,'//*[@id="infos"]/div[1]/div/ul/li')



#resolvendo a da e hora do ticket
arr_elements = len(dt_ticket)

for i in range(arr_elements):
    dt_ticket = dt_ticket[i].text
    dt_ticket = dt_ticket.splitlines()
    dt_ticket = dt_ticket[2]
    dt_ticket = dt_ticket.split()
    
    data_ticket = dt_ticket[5]
    hora_ticket = dt_ticket[6]

data_ticket = data_ticket.split('/')
data_ticket = data_ticket[2] + '-' + data_ticket[1] + '-' + data_ticket[0] + ' ' + hora_ticket


#resolvendo establishment
arr_establishment = nav.find_elements(libs.By.XPATH, '//*[@id="u20"]')

arr_elements = len(arr_establishment)

for i in range(arr_elements):
    establishment = arr_establishment[i].text

#definindo data do lançamento do ticket
dt_launch = libs.datetime.today().strftime('%Y-%m-%d-%H:%M:%S')

#resolvendo local da compra
local_compra = nav.find_elements(libs.By.XPATH, '//div[@class="txtTopo"]')
buy_address = nav.find_elements(libs.By.XPATH, '//div[@class="text"]')
arr_elements = len(buy_address)

for i in range(arr_elements):
    endereco = buy_address[i].text

#recuperando informações da compra
purchased_item = nav.find_elements(libs.By.XPATH, '//span[@class="txtTit2"]')

cod_productuto = nav.find_elements(libs.By.XPATH, '//span[@class="RCod"]')

quantity = nav.find_elements(libs.By.XPATH, '//span[@class="Rqtd"]')

measure = nav.find_elements(libs.By.XPATH, '//span[@class="RUN"]')

price = nav.find_elements(libs.By.XPATH, '//span[@class="RvlUnit"]')

total_value = nav.find_elements(libs.By.XPATH, '//span[@class="valor"]')

compras = len(purchased_item)

for i in range(compras):
    #print(cod_productuto[i].text + " : " + purchased_item[i].text + " : " +  quantity[i].text + " : " +  measure[i].text + " : " + qntXmeasure[i].text + " : " + total_value[i].text)
    
    df_cod_product[i] = cod_productuto[i].text
    
    df_purchased_item[i] = purchased_item[i].text

    df_quantity[i] = quantity[i].text

    df_measure[i] = measure[i].text

    df_price[i] = price[i].text

    df_total_value[i] = total_value[i].text

nav.close()

#Cria um data frame
ticket_lancamento = {
    'fk_id_account': classification.escolha_id_account
    , 'fk_id_transaction_type': classification.escolha_id_transaction_type
    , 'fk_id_subcategory': [classification.escolha_id_sub_category]
    , 'url_nfe': url_nfe
    , 'establishment': establishment
    , 'buy_address': endereco
    , 'dt_ticket': data_ticket
    , 'dt_launch': dt_launch
}
df_transaction = libs.pd.DataFrame(data=ticket_lancamento)

##insere lancamento
functions.queries.insert_trancao(df_transaction)

##Resgata as accounts registradas em BD
url_cara = functions.queries.get_last_transaction()
fk_id_transaction = url_cara.at[0,'id_transaction']

#criando DataFrame de ticket
ticket.insert(0, "cod_product", df_cod_product)
ticket.insert(1, "purchased_item", df_purchased_item)
ticket.insert(2, "quantity", df_quantity)
ticket.insert(3, "measure", df_measure)
ticket.insert(4, "price", df_price)
ticket.insert(5, "total_value", df_total_value)
ticket.insert(6, "fk_id_transaction", fk_id_transaction)

#Limpando coluna: cod_product
ticket['cod_product'] = ticket['cod_product'].str.replace('Código: ', '')
ticket['cod_product'] = ticket['cod_product'].str.replace('(', '')
ticket['cod_product'] = ticket['cod_product'].str.replace(')', '')


#Limpando coluna: quantity
ticket['quantity'] = ticket['quantity'].str.replace('Qtde.:', '')
ticket['quantity'] = ticket['quantity'].str.replace(',', '.')


#Limpando coluna: measure
ticket['measure'] = ticket['measure'].str.replace('UN: ', '')


#Limpando coluna: price
ticket['price'] = ticket['price'].str.replace('Vl. Unit.: ', '')
ticket['price'] = ticket['price'].str.replace(',', '.')


#Limpando coluna: total_value
ticket['total_value'] = ticket['total_value'].str.replace(',', '.')

functions.queries.set_ticket(ticket)