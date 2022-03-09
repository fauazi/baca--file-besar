import psycopg2
import re
import string


con = psycopg2.connect(
    host = "localhost",
    database = "bacafile",
    user = "postgres",
    password = "garma12345")

print("sudah terhubung")

cur = con.cursor()
frequency = {}
document_text = open('file1.txt', 'r')
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 
for words in frequency_list:
    kata = words
    jkata = frequency[words]
    cur.execute(
        "INSERT INTO hasildata4 (kalimat, jumlah_kalimat)"
        f"VALUES('{kata}', {jkata})",
        )
con.commit()
print("data sudah ditambahkan")
con.close()