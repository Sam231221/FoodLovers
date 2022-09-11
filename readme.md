You need to install Application Stack Manager  to install Postgis.
Video Source: https://www.youtube.com/watch?v=tTUM9XfDvqk

Then, type the following command.
i. psql;
ii. CREATE DATABASE CMS;
iii. CREATE USER Sam WITH PASSWORD 'sammer123';
iv. grant all privileges on database CMS to Sam;
v. CREATE EXTENSION postgis;

PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL