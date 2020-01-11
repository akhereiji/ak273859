Data Modeling with Postgres

Introduction
A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis, and bring you on the project. Your role is to create a database schema and ETL pipeline for this analysis. You'll be able to test your database and ETL pipeline by running queries given to you by the analytics team from Sparkify and compare your results with their expected results.

Project Description
In this project, you'll apply what you've learned on data modeling with Postgres and build an ETL pipeline using Python. To complete the project, you will need to define fact and dimension tables for a star schema for a particular analytic focus, and write an ETL pipeline that transfers data from files in two local directories into these tables in Postgres using Python and SQL.

FACT TABLE: 

songplay (songplay_id pk)

DIMENSION TABLES:

songs (song_id pk)
artists (artist_id pk)
time (time_id)
users (user_id)

The first step is that you need to draw ERD diagram with a star schema;
songplay as a fact table and the others as dimension table

The file path are written in JSON and log format. These files need to be loaded to the created database -Sparkify- in order to run it thru panda library df.

<<<song_data/A/B/C/TRABCEI128F424C983.json song_data/A/A/B/TRAAAVO128F93133D4.json>>>

And below is an example of what a single song file, TRAAAVO128F93133D4.json, looks like.

<<<RESULTS HAVE BEEN PRESENTED IN THE "test.ipnyp" as an example>>>

And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.

RESULTS HAVE BEEN PRESENTED IN THE "test.ipnyp" as an example

The aim of the project is to understand the ability to build relationships with data and extract the required data based on the requirements. 

Files description

1) Create_tables.py (This file is for creating and droping tables for the sparkify database)
2) etl.ipnyb (This file is just to test the program in terms of reading and extracting the files from the DB)
3) etl.py(This file is a translated version of etl.ipynb which helps to run the test.ipynb file)...This needs to run thru the command line. 
4)sql_queries.py (This file is for creating variables for tables and building the ERD)
5) test.ipynb(for testing the result of the project)
6) Untitled.ipynb (This file is for internal quality check)