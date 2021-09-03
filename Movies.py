import sqlite3 as db
from sqlite3 import Error

#creating connection with sqlite3 and creating database
try:
    conn=db.connect('Favourite_movies')
    print("Successfully established connection")
except Error:
    print(Error)

#Creating cursor object
cur=conn.cursor()

#create table
try:
    #if table already exists
    cur.execute("DROP TABLE MOVIES")
    cur.execute('''CREATE TABLE MOVIES
                   (ID INTEGER PRIMARY KEY,
                    MOVIE_NAME VARCHAR(25),
                    ACTOR VARCHAR(30),
                    ACTRESS VARCHAR(30),
                    DIRECTOR VARCHAR(30),
                    YEAR INTEGER)''')
    print("Successfully created Movies table")
except Error as err:
    print(err)

#function to insert  data into MOVIES table
def insert_data(name,actor,actress,director,year):
    try:
        query=f'''INSERT INTO MOVIES(MOVIE_NAME,ACTOR,ACTRESS,DIRECTOR,YEAR) VALUES("{name}","{actor}","{actress}","{director}",{year})'''
        cur.execute(query)
        print("Successfully inserted movie data")
    except Error as err:
        print(err)

#function to select data from MOVIES table
def select_data(query):
    try:
        result=cur.execute(query)
        for row in result:
            print(row)
    except Error as err:
        print(err)

#inserting data
insert_data('Shershaah','Sidharth Malhotra','Kiara Advani','Vishnuvardhan',2021)
insert_data('Bhajrangi Bhaijaan','Salman Khan','Kareena Kapoor','Kabir Khan',2015)
insert_data('Bhaag Milkha Bhaag','Farhan Akhtar','Sonam kapoor','Rakeysh Omprakash Mehra',2013)
insert_data('Tere Naam','Salman Khan','Bhumika Chawla','Satish Kaushik',2003)
insert_data('Om Shaanti Om','Sharukh khan','Deepika Padukone','Farah Khan',2007)

#select all the rows
print('Selecting all rows')
print('******************************************************************************************************************')
query1='''SELECT * FROM MOVIES'''
select_data(query1)
print('******************************************************************************************************************')

#select row of movie of Salman khan
print('Movies of Salman Khan')
print('******************************************************************************************************************')
query1='''SELECT * FROM MOVIES WHERE actor='Salman Khan' '''
select_data(query1)
print('******************************************************************************************************************')


#commit the changes
conn.commit()
#close connection
conn.close()