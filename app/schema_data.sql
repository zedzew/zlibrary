CREATE TABLE authors (
	id INTEGER NOT NULL,
	name VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE users (
	id INTEGER NOT NULL,
	name VARCHAR(50),
	email VARCHAR(120),
	password VARCHAR(32),
	PRIMARY KEY (id),
	UNIQUE (name),
	UNIQUE (email)
);
CREATE TABLE books (
	id INTEGER NOT NULL,
	title VARCHAR(50) NOT NULL,
	PRIMARY KEY (id)
);
CREATE TABLE books_authors (
	fk_book INTEGER,
	fk_author INTEGER,
	FOREIGN KEY(fk_book) REFERENCES books (id),
	FOREIGN KEY(fk_author) REFERENCES authors (id)
);
INSERT INTO users (name, email, password) VALUES ('test', 'test@test.test', 'test');
