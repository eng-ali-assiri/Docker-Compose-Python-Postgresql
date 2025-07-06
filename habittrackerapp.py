import time
import os
import psycopg2

# Connect to an existing database
time.sleep(5)
conn = psycopg2.connect(
    host=os.environ["DB_HOST"],
    dbname=os.environ["DB_NAME"],
    user=os.environ["DB_USER"],
    password=os.environ["DB_PASSWORD"],
    port=5432
)

# Open a cursor to perform database operations
cur = conn.cursor()

# Execute a command: this creates a new table
cur.execute("CREATE TABLE tracker (id INT PRIMARY KEY,name  VARCHAR(255), score INT, total INT);")

# Pass data to fill a query placeholders and let Psycopg perform
cur.execute("INSERT INTO tracker (id,name,score,total) VALUES (%s, %s,%s,%s)",(1, "Sami",7 ,8 ))

# Print * from tracker table
cur.execute("SELECT * FROM tracker")
rows = cur.fetchall()
for row in rows:
    print(row)

#print("11hello")

# Make the changes to the database persistent
conn.commit()
# Close communication with the database
cur.close()
conn.close()






#import psycopg2


#TRY 1
#conn=psycopg2.connect("dbname=postgres user=postgres")
 # database='postgres',
  #user='postgres',
  #password='1234',
#)


#TRY 2
#conn=psycopg2.connect("dbname=postgres user=postgres")


#TRY 3
#conn = psycopg2.connect(host="localhost",dbname="postgres")