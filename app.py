from flask import Flask, request
import axisDatas

app = Flask(__name__)
app.config['JSON_AS_ASCII']=False

@app.route('/file-datas', methods=['POST'])
def home():
  fileName = request.args['file_name']
  fileURL = request.args['file_URL']
  tspSetting = request.args['tsp_setting']
  defectSetting = request.args['defect_setting']

  print("nextjs 로부터 받아온 file", fileName)
  result = axisDatas.getData(fileName, fileURL, tspSetting, defectSetting)

  return result

if __name__ == '__main__':
  app.run(debug=False, host='0.0.0.0')