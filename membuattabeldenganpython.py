import psycopg2


con = psycopg2.connect(
    host = "localhost",
    database = "bacafile",
    user = "postgres",
    password = "garma12345")

print("sudah terhubung")

cur = con.cursor()

cur.execute("""

CREATE TABLE hasildata3
(
KALIMAT TEXT PRIMARY KEY,
JUMLAH_kalimat INT NOT NULL

)

""")

con.commit()
print("tabelnya sudah jadi")