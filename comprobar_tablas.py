import oracledb

conn = oracledb.connect(
    user="SYSTEM",
    password="1234509876",
    dsn="localhost:1521/XEPDB1"
)

cursor = conn.cursor()

cursor.execute("SELECT table_name FROM user_tables")

print("Tablas disponibles:")
for table in cursor.fetchall():
    print(table[0])
