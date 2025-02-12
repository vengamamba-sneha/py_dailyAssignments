create database student;
use student;

create table stdinfoo( id int primary key, name varchar(20) not null, email varchar(20) not null, age int not null, gender varchar(10) not null,
phno varchar(10) not null, dept varchar(10) not null, cgpa float not null);

insert into stdinfoo(id,name,email,age,gender,phno,dept,cgpa) values (1,'luffy','luffy@gmail.com',19,'male',3333333444,'CSE',9.9);
insert into stdinfoo(id,name,email,age,gender,phno,dept,cgpa) values (2,'zoro','zoro@gmail.com',19,'male',3333933444,'CSC',8.9);
insert into stdinfoo(id,name,email,age,gender,phno,dept,cgpa) values (3,'mira','mira@gmail.com',19,'female',3333533444,'CSM',9.4);
insert into stdinfoo(id,name,email,age,gender,phno,dept,cgpa) values (4,'mori jin','jin@gmail.com',18,'male',3553333444,'CSE',9.9);
insert into stdinfoo(id,name,email,age,gender,phno,dept,cgpa) values (5,'nami','nami@gmail.com',18,'female',3003333444,'CSD',8.9);
insert into stdinfoo(id,name,email,age,gender,phno,dept,cgpa) values (6,'ussop','ussop@gmail.com',20,'male',3333333000,'CSC',8.3);
insert into stdinfoo(id,name,email,age,gender,phno,dept,cgpa) values (7,'sanji','sanji@gmail.com',20,'male',3933333444,'CSM',9.1);
insert into stdinfoo(id,name,email,age,gender,phno,dept,cgpa) values (8,'brook','brook@gmail.com',22,'male',3333399444,'CSD',7.9);

select* from stdinfoo;
show tables