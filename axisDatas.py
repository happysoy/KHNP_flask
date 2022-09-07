import requests
import json

def getData():
  url = "http://3.34.118.72:5000/echo_call" #ec2 인스턴스의 퍼블릭 ip/탄력적 ip를 써야한다
  data = {"url": 'https://khnp.s3.ap-northeast-2.amazonaws.com/HB-01-23-CD-A1-01-014018.dat',
          "name": 'HB-01-23-CD-A1-01-014018'}
  res = requests.post(url=url, json=data)

  received = res.content
  convert = json.loads(received.decode("utf-8"))

  return convert['CH3Y']