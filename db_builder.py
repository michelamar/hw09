#THERE IS A COMPILETIME ERROR I DON'T UNDERSTAND WHEN I TRY TO POPULATE THE TABLE, SO I COMMENTED THOSE PARTS
#OUT


import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


f="discobandit.db"

db = sqlite3.connect(f) #open if f exists, otherwise create
c = db.cursor()    #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

with open('peeps.csv') as csvfile:
    peeps = csv.DictReader(csvfile)

    command = "CREATE TABLE peepsDb (name STRING, age INTEGER, id INTEGER);"
    c.execute(command) #run statement to create table
    #for row in peeps:
      #  contents = '(' + row['name'] + ", " + row['age'] + ", " +  row['id']+ ');'
      #  c.execute("INSERT INTO peepsDB VALUES" + contents) #run statement to populate table
        

with open('courses.csv') as csvfile:
    courses = csv.DictReader(csvfile)

    command = "CREATE TABLE coursesDb (code STRING, mark INTEGER, id INTEGER);"
    c.execute(command)
    #for row in courses:
     #   command = "INSERT INTO peepsDb VALUES (" + row['code'] + ", " + row['mark']+ ", " + row['id'] + ");"
     #   c.execute(command)


command = ""          #put SQL statement in this string
c.execute(command)    #run SQL statement

#==========================================================
db.commit() #save changes
db.close()  #close database
peeps.close() #close file
courses.close() #close file


