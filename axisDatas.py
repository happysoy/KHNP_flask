import requests
import json

# 폴더 이름도 받아와야함
def getData(fileName,fileURL):
  url = "http://3.34.118.72:5000/echo_call" #ec2 인스턴스의 퍼블릭 ip/탄력적 ip를 써야한다
  data = {"url": fileURL,
          "name": fileName}
  res = requests.post(url=url, json=data)

  received = res.content
  convert = json.loads(received.decode("utf-8"))

  return convert