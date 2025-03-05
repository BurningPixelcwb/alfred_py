 -- Realiza inserçõe na tabela category
INSERT INTO category (id_category, category_name, situation) VALUES
	  (1, 'Moradia', 'A')
	, (2, 'Amor', 'A')
	, (3, 'Diferentao', 'A')
	, (4, 'Emprego', 'A')
	, (5, 'Relacionamento', 'A')
	, (6, 'Saude', 'A');

 -- Realiza inserçõe na tabela account
INSERT INTO account (id_account, account_name, situation) VALUES
(1, 'Bradesco account Corrente', 'A'),
(2, 'Itau account Corrente', 'A'),
(3, 'Carteira', 'A'),
(4, 'Cofrinho', 'A'),
(5, 'VA - Vale Alimentacao', 'A'),
(6, 'VR - Vale Refeicao', 'A'),
(7, 'Auxílio Home Office', 'A');
-- Realiza inserçõe na tabela SUBcategory
INSERT INTO subcategory (id_subcategory, subcategory_name, fk_id_category) VALUES
(1, 'Alimentacao', 2),
(2, 'Cinema', 2),
(3, 'Agua', 1),
(4, 'Gasolina', 1),
(5, 'Alimentacao', 1),
(6, 'Alimentacao', 3),
(7, 'Estacionamento', 3),
(8, 'Gasolina', 3),
(9, 'Marketing Digital', 3),
(10, 'Reuniao', 3),
(11, 'Transporte', 3),
(12, 'Figurino', 3),
(13, 'Refeicao', 1),
(14, 'Bump', 4),
(15, 'Alimentacao', 5),
(16, 'Remedios', 6),
(17, 'Equipamento', 6),
(18, 'Salario', 4);

-- Realiza inserçõe na tabela TIPO transaction
INSERT INTO transaction_type (id_transaction_type, transaction_type_name) VALUES
(1, 'Despesa'),
(2, 'Receita'),
(3, 'Transferencia');