from flask import Flask, request, Response
import requests
import json
import time

app = Flask(__name__)
app.config['JSON_AS_ASCII']=False

@app.route('/file-datas', methods=['POST'])
def home():
  fileName = request.args['file_name']
  fileURL = request.args['file_URL']
  tspSetting = request.args['tsp_setting']
  defectSetting = request.args['defect_setting']

  start = time.time();

  url = "http://125.6.38.196:5000/echo_call" #ec2 인스턴스의 퍼블릭 ip/탄력적 ip를 써야한다
  data = {"url": fileURL,
          "name": fileName,
          "tspSetting":tspSetting,
          "defectSetting":defectSetting
          }
  res = requests.post(url=url, json=data)

  received = res.content
  convert = json.loads(received.decode("utf-8"))

  end=time.time()

  print("flask 소요 시간 : " , end-start)

  return Response(json.dumps(convert), status=res.status_code, mimetype='application/json')


if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0', threaded=True)