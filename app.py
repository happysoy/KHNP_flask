from flask import Flask
import axisDatas
app = Flask(__name__)

@app.route('/file-datas')
def home():

  result = axisDatas.getData()

  return result

if __name__ == '__main__':
  app.run(debug=True)