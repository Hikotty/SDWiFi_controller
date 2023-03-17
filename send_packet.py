def send_packet():
    import requests
    import time

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

    err = 0
    for i in range(10**10):
        print("kkk")
        with open("packet_flag.txt") as file:
            flag = file.read()
        if int(flag) == 1:
            try:
                r = requests.get('http://192.168.11.5/api/v1/cw/send?length=2000',headers=header,timeout=((1,1)))
                print(r,int(time.time()))
            except:
                if KeyboardInterrupt:
                    print(err)
                    exit()
                else:
                    print("errored",int(time.time()))
                    err += 1
        else:
            time.sleep(1)