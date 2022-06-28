import requests
import time

API_TOKEN = '1-083ed198-014c-4307-8453-bfda8cddd-rc486ccc47e726ed96910f02bba5'
SECRET_KEY = '59qdmMoAjLig2jeAGghP+98FVeslm5B1Xg8VKZGSn2iKY77AuWzgqDFyHzyvc+CJmUxpNF1haInpV01qMFZPZQ=='

r = requests.get('https://api.gopax.co.kr/trading-pairs')
"""
res_list = r.json()

for rl in res_list:
    print(rl)

"""

# 호가창

"""
r = requests.get('https://api.gopax.co.kr/trading-pairs/BTC-KRW/book')

print(r.json()['bid'])
print(r.json()['ask'])
"""

now_time = round(time.time() * 1000)
start = int(now_time)-60*50*1000
end = int(now_time)

print(start)
print(end)

r = requests.get('https://api.gopax.co.kr/trading-pairs/BTC-KRW/candles?start='+str(start)+'&end='+str(end)+'&interval=1')
print(len(r.json()))
print(r.json())

"""
[
    <Time>
    <Low>
    <High>
    <Open>
    <Close>
    <Volume>  
]
"""