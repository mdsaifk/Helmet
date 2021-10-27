from flask import Flask,render_template,request
from flask_cors import cross_origin
from detection import mobilenet, Decode
from wsgiref import simple_server
import os
os.putenv('LANG', 'en_US.UTF-8')
os.putenv('LC_ALL', 'en_US.UTF-8')

app = Flask(__name__)

@app.route('/',methods=['GET'])
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/result',methods=['GET','POST'])
@cross_origin()
def result():
    if request.method == 'POST':
        image = request.json['image']
        img = Decode(image).copy()
        #img = cv2.resize(img, (480, 320),interpolation=cv2.INTER_NEAREST)
        mobilenet(img)
        return render_template('index.html')
    return render_template('index.html')



#if __name__=="__main__":
    #app.run(host="0.0.0.0",port=6003)

if __name__ == "__main__":
    port = int(os.getenv("PORT"))
    #clApp = ClientApp()
    host = '0.0.0.0'
    httpd = simple_server.make_server(host=host,port=port, app=app)
    httpd.serve_forever()
# Author: Saif khan
# Date : 2-09-2021