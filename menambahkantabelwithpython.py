import psycopg2


con = psycopg2.connect(
    host = "localhost",
    database = "bacafile",
    user = "postgres",
    password = "garma12345")

print("sudah terhubung")

cur = con.cursor()

cur.execute("INSERT INTO hasildata (kalimat, jumlah_huruf) VALUES('Cerita pendek anak selanjutnya yaitu :', 39)")
cur.execute("INSERT INTO hasildata (kalimat, jumlah_huruf) VALUES('Diceritakan seekor penguasa hutan yang hebat, kuat, dan pemberani.', 167)")
cur.execute("INSERT INTO hasildata (kalimat, jumlah_huruf) VALUES('Ia adalah sang raja rimba yaitu Singa.', 39)")
cur.execute("INSERT INTO hasildata (kalimat, jumlah_huruf) VALUES('Singa adalah penguasa hutan yang juga dihormati oleh penghuni hutan.', 69)")
cur.execute("INSERT INTO hasildata (kalimat, jumlah_huruf) VALUES('Ia merupakan pelindung dari kejahatan seperti pemburu.', 55)")
cur.execute("INSERT INTO hasildata (kalimat, jumlah_huruf) VALUES('Tak segan-segan, Singa pernah menerkam pemburu yang hendak merusak hutan dan memburu hewan di hutan.', 101)")
cur.execute("INSERT INTO hasildata (kalimat, jumlah_huruf) VALUES('Tindakannya itu memang harus dimiliki oleh seorang Raja sebagai penguasa hutan.', 80)")
cur.execute("INSERT INTO hasildata (kalimat, jumlah_huruf) VALUES('Temukan cerita lengkapnya pada buku Tempel & Warnai Lion King: Simba Sang Raja', 78)")
con.commit()
print("data sudah ditambahkan")
con.close()