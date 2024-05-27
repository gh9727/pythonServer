from flask import Flask, send_file
import cv2
import numpy as np
import io

app = Flask(__name__)

@app.route('/')
def home():
   return 'This is Home!'

@app.route('/opencv')
def opencv():
    # 이미지 파일 열기
    image_path = 'static/jeremih.png'
    image = cv2.imread(image_path,0) # -> 일반 이미지 + 0 은 이미지를 흑백으로 불러옴

    th,mask = cv2.threshold(image,0,255,cv2.THRESH_OTSU)
    # 이미지를 png 포맷으로 메모리 스트림에 저장
    is_success, buffer = cv2.imencode(".png", mask)
    io_buf = io.BytesIO(buffer)


    # 이미지 파일을 HTTP 응답으로 반환
    return send_file(io_buf, mimetype='image/png', as_attachment=False, download_name='jeremih.png')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4444, debug=True)