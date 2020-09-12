import sqlite3

#connect to database
#create a file data.db in current directory which will be database
connection = sqlite3.connect('data.db')

#help to run any query from database
cursor = connection.cursor()

#create table with 3 columns id, username, id and password
create_table = "CREATE TABLE users (id int , username text , password text)"
#execute the query
cursor.execute(create_table)

user =(1,'jose','asdf')

insert_query = "INSERT INTO users VALUES (?,?,?)"

cursor.execute(insert_query,user)


users = [
(2,'j2ose','asdf4'),
(3,'jo456se','a3sdf')

]

#for many users to insert we use

cursor.executemany(insert_query,users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print(row)
#to save the data in disk
connection.commit()

connection.close()
