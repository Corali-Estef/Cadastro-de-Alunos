CREATE TABLE Dados_Alunos
(
	Cod_Aluno INTEGER IDENTITY(1,1) ,
	Nome VARCHAR(100),
	Data VARCHAR(10),
	Idade INTEGER,
	Objetivo VARCHAR(1000),
	Genero INTEGER,
	Email VARCHAR(100)
)
go

ALTER TABLE Dados_Alunos
ADD CONSTRAINT PK_Cod_Aluno PRIMARY KEY (Cod_Aluno)


GO



CREATE TABLE Genero
(
	Cod_Genero INTEGER IDENTITY(1,1),
	Genero VARCHAR(30)
)
go

ALTER TABLE Genero
ADD CONSTRAINT PK_Cod_Genero PRIMARY KEY (Cod_Genero)
GO

IF NOT EXISTS ( SELECT * FROM SYS.foreign_keys WHERE parent_object_id = OBJECT_ID('Dados_Alunos') AND name = 'FK_Cod_Aluno') 
BEGIN
	ALTER TABLE Dados_Alunos
	ADD CONSTRAINT FK_Cod_Aluno FOREIGN KEY(Genero)
	REFERENCES GENERO(Cod_Genero)
END
GO





INSERT INTO Genero ( Genero) VALUES ('MASCULINO')

GO



INSERT INTO Genero ( Genero) VALUES ('FEMININO')
go
INSERT INTO Genero ( Genero) VALUES ('outros')

GO

select * from Dados_Alunos