import requests               # url: get 요청
import csv                    # csv로 저장
import os                     # 폴더 생성
from datetime import datetime # 시간 변환

API_KEY_W = os.getenv("API_KEY_W")
city = "seoul"
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY_W}&units=metric"

response = requests.get(url)
result = response.json()

temp = result["main"]["temp"] # 현재 기온
humidity = result["main"]["humidity"] # 습도
weather = result["weather"][0]["main"] # 날씨 상태
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 현재 시간

header = ["current_time", "weather", "temp", "humidity"] # csv header

csv_exist = os.path.exists("seoul_weather.csv")
# w : write, r : read, wb : write byte, a : write(있다면 덮어쓰기)
with open ("seoul_weather.csv", "a") as file:
    writer = csv.writer(file)

    # csv가 한 번도 안 만들어졌다면, 헤더 추가
    if not csv_exist: 
        writer.writerow(header)
    
    writer.writerow([current_time, weather, temp, humidity])
    print("서울 기온 저장 완료")
