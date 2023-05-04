create database Unes;
use Unes;

create table Contato(
	email varchar(50) not null,
    assunto varchar(50) not null,
    descricao varchar(300) not null
);

select * from Contato;
