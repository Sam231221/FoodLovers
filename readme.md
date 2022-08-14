You need to install Application Stack Manager  to install Postgis.
Video Source: https://www.youtube.com/watch?v=tTUM9XfDvqk

Then, 
psql
CREATE DATABASE CMS;
CREATE USER Sam WITH PASSWORD 'sammer123';
grant all privileges on database CMS to Sam;
CREATE EXTENSION postgis;

PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL