from flask import Flask, request
import axisDatas
app = Flask(__name__)
app.config['JSON_AS_ASCII']=False

@app.route('/file-datas', methods=['POST'])
def home():
  fileName = request.args['file_name']
  fileURL = request.args['file_URL']

  print("nextjs 로부터 받아온 정보", fileName, fileURL)
  result = axisDatas.getData(fileName, fileURL)

  return result

if __name__ == '__main__':
  app.run(debug=True)