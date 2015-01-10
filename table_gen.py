__author__ = 'kic'

from forum_app.api_packs.db_queries.queries import exec_sql

if __name__ == '___main__':
    exec_sql(
        ' create table User(id int auto_increment PRIMARY KEY, name varchar(255), isAnonymous tinyint(1)' /
        ' not null default 0, email varchar(255) unique, about mediumtext, username varchar(255))')

    exec_sql(
        ' create table Thread(id int auto_increment PRIMARY KEY, date datetime, title varchar(255),' /
        ' isClosed tinyint(1) not null default 0, isDeleted tinyint(1) not null default 0, message mediumtext,' /
        ' slug varchar(255), likes int(11) not null default 0, dislikes int(11) not null default 0,' /
        ' points int(11) not null default 0, user varchar(255), forum varchar(255), posts int(11) not null default 0);')

    exec_sql(
        ' create table Subscribe(id int auto_increment PRIMARY KEY, thread int(11), user varchar(255),' /
        ' isDeleted tinyint(1) not null default 0);'
    )

    exec_sql(' create table Post(id int auto_increment PRIMARY KEY, date datetime,' /
             ' isApproved tinyint(1)  not null default 0, isDeleted tinyint(1)  not null default 0,' /
             ' isEdited tinyint(1)  not null default 0, isHighlighted tinyint(1)  not null default 0,' /
             ' isSpam tinyint(1)  not null default 0, message mediumtext, likes int(11) not null default 0,' /
             ' dislikes int(11) not null default 0, points int(11) not null default 0,' /
             ' user varchar(255), forum varchar(255) not null, parent int(11),  thread int(11) );')

    exec_sql('create table Forum(id int auto_increment PRIMARY KEY, name varchar(255), short_name varchar(255),' /
             ' user varchar(255));')

    exec_sql('create table Followers(id int auto_increment PRIMARY KEY, follower varchar(255), followee varchar(255),' /
             ' isDeleted tinyint(1) not null default 0);')

