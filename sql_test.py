import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="root",
  database="test_schema"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM new_table")
#mycursor.execute("SELECT * FROM measurements WHERE Time BETWEEN '2019-10-07 16:55:43' AND '2019-10-07 16:56:04'")
df = pd.DataFrame(mycursor.fetchall())
df.columns = mycursor.column_names


mydb.close()