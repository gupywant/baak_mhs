import mysql.connector
import requests
from bs4 import BeautifulSoup
#database
kelas = "2ka"
mydb = mysql.connector.connect(
  host="localhost",
  user="unnamed48",
  passwd="12345678",
  db="mahasiswa"
)
mycursor = mydb.cursor()
def crawling(kelas):
	url = "http://baak.gunadarma.ac.id/cariKelasBaru?tipeKelasBaru=Kelas&teks="+kelas
	r = []
	r.append(s.get(url))
	url2 = "http://baak.gunadarma.ac.id/cariKelasBaru?tipeKelasBaru=Kelas&page=2&teks="+kelas
	r.append(s.get(url2))
#	soup = BeautifulSoup(r[0], 'lxml')
#	h5 = soup.findAll("h5")
#	try:
#	    dataout = h5[0].text
#	except IndexError:
#	    dataout = "fail"
	return r
def parsing(r):
	data = []
	codex = 1
	for i in range(0,2):
		data.append(r[i].text)
		soup = BeautifulSoup(data[i], 'lxml')
		td = soup.findAll("td")
		pan = len(td)
		i = 0
		while i < pan/2:
			print "================"
			absen = td[i].text
			npm = td[i+1].text
			nama = td[i+2].text
			lama = td[i+3].text
			baru = td[i+4].text
			print "absen : " + absen
			print "npm : " +npm
			print "nama : " +nama
			print "kelas lama : "+lama
			print "kelas baru : "+baru
			sql = "insert into example values(%s,%s,%s,%s,%s)"
			valu = (absen,npm,nama,lama,baru)
			mycursor.execute(sql, valu)
			mydb.commit()
			i = i+5
for j in range(32,40):
	s = requests.session()
	if(j<=9):
		kelas += str(j)
	else:
		kelas += str(j)
	#passing & crawling
	r = crawling(kelas)
	codex = parsing(r)
	if(codex==0):
		print ""
		print "crawling finished!!!"
		break
print("record inserted.")
