CREATE TABLE Usuario (
nome varchar,
senha varchar,
id integer PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE video (
url varchar,
categoria varchar,
id integer PRIMARY KEY AUTOINCREMENT,
id_usuario integer
);
