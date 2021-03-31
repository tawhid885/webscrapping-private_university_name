from bs4 import BeautifulSoup
import requests
import csv




source=requests.get('http://www.ugc-universities.gov.bd/private-universities').text
soup=BeautifulSoup(source,'lxml')

csv_file =open('private_university.csv','w')
csv_writer=csv.writer(csv_file)
csv_writer.writerow(['No','University Name','Website'])

table_body=soup.find('tbody')
rows = table_body.find_all('tr')


for row in rows:
    cols=row.find_all('td')
    cols=[x.text.strip() for x in cols]
    print(cols[1])
    try:
        csv_writer.writerow([cols[0],cols[1],cols[2]])
    except UnicodeEncodeError:
        pass

csv_file.close()
