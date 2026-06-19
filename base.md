pip install mysql-connector-python

ou

python -m pip install mysql-connector-python



**Banco:**

\#CREATE DATABASE saep\_estoque;



CREATE TABLE produtos (

&#x09;id INT AUTO\_INCREMENT PRIMARY KEY,

&#x20;   nome VARCHAR(100) NOT NULL,

&#x20;   categoria VARCHAR(100) NOT NULL,

&#x20;   quantidade INT NOT NULL,

&#x20;   preco DECIMAL(10, 2) NOT NULL

);



DESCRIBE produtos;  #Descreve o banco!



\#Update simples

UPDATE produtos SET nome = "danillo", categoria = "lindo", quantidade = "1", preco = "100"

WHERE id = 1;



SELECT \* FROM produtos; #SELECT 



TRUNCATE produtos; #Limpa apenas os dados



INSERT INTO produtos(nome, categoria, quantidade, preco)

VALUES ();



USE saep\_estoque;

