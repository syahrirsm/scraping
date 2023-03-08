import mysql.connector

# membuat koneksi ke database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="bbc_link"
)

# membuat kursor
mycursor = mydb.cursor()

# melakukan query untuk mengambil data dari tabel
mycursor.execute("SELECT * FROM data")

# mengambil semua hasil query
result = mycursor.fetchall()

# menampilkan hasil query
for row in result:
  print(row)
