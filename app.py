from fastapi import FastAPI
import requests
import json

app = FastAPI()

@app.post("/file-datas")
async def home(file_name: str, file_URL:str, tsp_setting:str, defect_setting: str):
 
  url = "http://125.6.38.196:5000/echo_call" #ec2 인스턴스의 퍼블릭 ip/탄력적 ip를 써야한다
  data = {"url": file_URL,
          "name": file_name,
          "tspSetting":tsp_setting,
          "defectSetting":defect_setting
          }
  res = requests.post(url=url, json=data)

  received = res.content
  convert = json.loads(received.decode("utf-8"))

  return convert

