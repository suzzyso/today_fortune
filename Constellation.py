import requests
from bs4 import BeautifulSoup

from pymongo import MongoClient     # pymongo를 임포트 하기(패키지 인스톨 먼저 해야겠죠?)
client = MongoClient('mongodb://test:test@localhost', 27017)
#client = MongoClient('localhost', 27017)  # mongoDB는 27017 포트로 돌아갑니다.
db = client.Constellation                      # 'dbsparta'라는 이름의 db를 만듭니다.

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data_Aquarius = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%AC%BC%EB%B3%91%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Aries = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%96%91%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Pisces = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%AC%BC%EA%B3%A0%EA%B8%B0%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Taurus = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%ED%99%A9%EC%86%8C%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Gemini = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%8C%8D%EB%91%A5%EC%9D%B4%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Cancer = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EA%B2%8C%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Leo = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%82%AC%EC%9E%90%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Virgo = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%B2%98%EB%85%80%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Libra = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%B2%9C%EC%B9%AD%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Scorpius = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%A0%84%EA%B0%88%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Sagittarius = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%82%AC%EC%88%98%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)
data_Capricornus = requests.get('https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EC%97%BC%EC%86%8C%EC%9E%90%EB%A6%AC%20%EC%9A%B4%EC%84%B8',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup_Aquarius = BeautifulSoup(data_Aquarius.text, 'html.parser')
soup_Aries = BeautifulSoup(data_Aries.text, 'html.parser')
soup_Pisces = BeautifulSoup(data_Pisces.text, 'html.parser')
soup_Taurus = BeautifulSoup(data_Taurus.text, 'html.parser')
soup_Gemini = BeautifulSoup(data_Gemini.text, 'html.parser')
soup_Cancer = BeautifulSoup(data_Cancer.text, 'html.parser')
soup_Leo = BeautifulSoup(data_Leo.text, 'html.parser')
soup_Virgo = BeautifulSoup(data_Virgo.text, 'html.parser')
soup_Libra = BeautifulSoup(data_Libra.text, 'html.parser')
soup_Scorpius = BeautifulSoup(data_Scorpius.text, 'html.parser')
soup_Sagittarius = BeautifulSoup(data_Sagittarius.text, 'html.parser')
soup_Capricornus = BeautifulSoup(data_Capricornus.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
fortune_Aquarius = soup_Aquarius.select('#yearFortune > div')
fortune_Aries = soup_Aries.select('#yearFortune > div')
fortune_Pisces = soup_Pisces.select('#yearFortune > div')
fortune_Taurus = soup_Taurus.select('#yearFortune > div')
fortune_Gemini = soup_Gemini.select('#yearFortune > div')
fortune_Cancer = soup_Cancer.select('#yearFortune > div')
fortune_Leo = soup_Leo.select('#yearFortune > div')
fortune_Virgo = soup_Virgo.select('#yearFortune > div')
fortune_Libra = soup_Libra.select('#yearFortune > div')
fortune_Scorpius = soup_Scorpius.select('#yearFortune > div')
fortune_Sagittarius = soup_Sagittarius.select('#yearFortune > div')
fortune_Capricornus = soup_Capricornus.select('#yearFortune > div')

db.fortune.drop()

for fortune in fortune_Aquarius:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()
        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Pisces:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)



for fortune in fortune_Aries:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Taurus:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Gemini:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Cancer:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Leo:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Virgo:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Libra:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Scorpius:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Sagittarius:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)

for fortune in fortune_Capricornus:
    date = fortune.select_one('#yearFortune > div > div.thumb').text
    title = fortune.select_one('#yearFortune > div > div.detail.detail2 > h6 > ul > li.first_lst > a').text
    today_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(3)').text
    tomorrow_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(4)').text
    week_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(5)').text
    month_text = fortune.select_one('#yearFortune > div > div.detail.detail2 > p:nth-child(6)').text

    if date is not None:
        print(title, date)
        print('오늘의 운세 : ' + today_text)
        print('내일의 운세 : ' + tomorrow_text)
        print('이주의 운세 : ' + week_text)
        print('이달의 운세 : ' + month_text)
        print()

        doc = {
            'date': date,
            'title': title,
            'today_text': today_text,
            'tomorrow_text': tomorrow_text,
            'week_text': week_text,
            'month_text': month_text,
        }
        db.fortune.insert_one(doc)








