--careful, mysql has their own data types 
CREATE TABLE url(

    --id (should be integer)
    id int AUTO_INCREMENT UNIQUE,--auto increments your insert 

    --hash
    shortened_url varchar(7) UNIQUE,

    --original url 
    original_url varchar(1000) NOT NULL, -- not null meaning bu hui shi kong de 

    PRIMARY KEY(id,shortened_url)
    

);