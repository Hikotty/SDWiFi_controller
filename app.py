from flask import Flask, render_template
import json
from pathlib import Path
import requests
import time
import threading

app = Flask(__name__)


@app.route('/')
def main():
    return render_template("index.html")

@app.route('/start')
def start():
    # スレッドを開始し、処理を続ける
    t = threading.Thread(target=long_running_process)
    t.start()
    return 'Started!'

@app.route('/stop')
def stop():
    # 処理を停止するために、フラグをセットする
    global stop_flag
    stop_flag = True
    return 'Stopped!'

def long_running_process():
    global stop_flag
    stop_flag = False
    err = 0
    header = {
        "Accept":"*/*",
        "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "ja,en-US;q=0.9,en;q=0.8",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQ=",
        "Connection": "keep-alive",
        "Cookie": "PHPSESSID=l54da3gu7ci6pqlfcm21ector4",
        "Host": "192.168.11.5",
        "Referer": "http://192.168.11.5/cw/send",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest"
    }

    while not stop_flag:
        try:
            r = requests.get('http://192.168.11.5/api/v1/cw/send?length=2000',headers=header,timeout=((1,1)))
            print(r,int(time.time()))
        except:
            print("errored",int(time.time()))
            err += 1
    print("ertroed",err)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0',port=8080)

