import requests
from bs4 import BeautifulSoup


Year=22
Month=11
Day=3

Year=str(Year)
Month=str(Month)
Day=str(Day)

Month=Month.zfill(2)
Day=Day.zfill(2)

url='http://transcripts.cnn.com/TRANSCRIPTS/{}/{}/sn.01.html'.format(Year+Month,Day)

resp=requests.get(url)
soup=BeautifulSoup(resp.text)
print('Request code is {}'.format(resp.status_code))

container=soup.find('div', style='padding-left:10px;').find_all('p',class_='cnnBodyText')

contents=''
for i in container:
    contents+='\n'+ i.get_text().strip()

contents=contents.replace("`","'")
contents=contents.replace('   ',' ')

file=open('{}{}{}_CNN.txt'.format(Year,Month,Day),'w')
file.write(contents)
file.close()
