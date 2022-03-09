import psycopg2


con = psycopg2.connect(
    host = "localhost",
    database = "bacafile",
    user = "postgres",
    password = "garma12345")

print("sudah terhubung")

cur = con.cursor()
with open('file1.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    count += 1
    baris = line
    jhuruf = len(line)
    cur.execute(
        "INSERT INTO hasildata3 (kalimat, jumlah_kalimat)"
        f"VALUES('{count}', {jhuruf})",
        )
con.commit()
print("data sudah ditambahkan")
con.close()