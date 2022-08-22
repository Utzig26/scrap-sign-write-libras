import csv
import requests
import concurrent.futures

URL = "https://www.signbank.org/signpuddle2.0/glyphogram.php?size=0.7&ksw="

def img_dowloader(src, filename):
	filename = filename.replace(" ","_")
	filename = filename.lower()
	try:
		image = requests.get(URL+src, stream=True)
		with open('photos/'+filename, 'wb') as img:
			for chunk in image:
				img.write(chunk)
			print(filename+' - '+src)
	except:
		pass 

ids = []
filenames = []
with open("tcc_ze.csv","r+",encoding="utf8") as f:
	signals = csv.reader(f, delimiter=',')
	for line in signals:
		ids.append(line[0])
		filenames.append(line[1])

no_threads = 1000
with concurrent.futures.ThreadPoolExecutor(max_workers=no_threads) as executor:
	cont = 0
	for i in range(0,len(ids)):
		executor.submit(img_dowloader, ids[i], filenames[i]+'-'+str(cont)+'.jpg')
		cont+=1

