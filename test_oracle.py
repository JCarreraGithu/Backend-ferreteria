import oracledb

conn = oracledb.connect(
    user="SYSTEM",
    password="1234509876",
    dsn="localhost:1521/XEPDB1"
)

print("Conectado correctamente a Oracle")
