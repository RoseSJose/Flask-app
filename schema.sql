drop table if exists posts;

create table posts(
    id serial primary key,
    name text not null,
    content text not null
);