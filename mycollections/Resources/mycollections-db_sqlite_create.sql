CREATE TABLE Usuario (
	nome varchar,
	id integer PRIMARY KEY AUTOINCREMENT
);

CREATE TABLE video (
	categoria varchar,
	url varchar,
	id integer PRIMARY KEY AUTOINCREMENT,
	id_usuario integer
);

