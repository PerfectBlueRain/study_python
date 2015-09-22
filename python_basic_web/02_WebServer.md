# Web Server
- BaseHTTPServer
- SimpleHTTPServer
- CGIHTTPServer

![](http://drive.google.com/uc?export=view&id=0B0CgSzgDruziXzM0M2NYa3FNdjA)
![](http://drive.google.com/uc?export=view&id=0B0CgSzgDruziQUZuTGxTRmhEb3M)

---

---

## BaseHTTPServer
- HTTPServer 객체를 생성할때 핸들을 지정
- BaseHTTPRequestHndler 핸들 http의 기본적인 응답을 할 수 있는 기능이 들어있다.
```python
class http.server.HTTPServer(server_address, RequestHandlerClass)
```
   - serve_forever() : 웹브라우저의 요청을 기다림, 요청이 들어오면 등록된 핸들러에 요청정보를 전달
   - do_GET() : GET요청이 들어오면 전달
   ```python
   class MyHandler(BaseHTTPRequestHandler):

       def do_GET(self):
           from urllib.parse import urlparse
           import sys

           parts = urlparse(self.path)
           keyword, value = parts.query.split('=',1)

           if keyword == "title" :
               html = MakeHtmlDoc(SearchBookTitle(value)) # keyword에 해당하는 책을 검색해서 HTML로 전환합니다.
               ##헤더 부분을 작성.
               self.send_response(200)
               self.send_header('Content-type', 'text/html')
               self.end_headers()
               self.wfile.write(html.encode('utf-8')) #  본분( body ) 부분을 출력 합니다.
           else:
               self.send_error(400,' bad requst : please check the your url') # 잘 못된 요청라는 에러를 응답한다.

   #####################################

   def startWebService():
       try:
           server = HTTPServer( ('localhost',8080), MyHandler)
           print("started http server....")
           server.serve_forever()

       except KeyboardInterrupt:
           print ("shutdown web server")
           server.socket.close()  # server 종료합니다.
   ```


## SimpleHTTPServer

- 앞절에서는 웹서버를 만들기 위해 MyHandler라는 핸들러를 코딩하였다. SimpleHTTPServer 모듈 내에는 SimpleHTTPRequestHandler 클래스가 정의
- 이 핸들러에는 do_GET() 및 do_HEAD() 함수가 정의 되어있어서 아래와 간단한 명령어로 코딩없이 웹서버를 작동시킬수 있다. 아래 명령어는 실행한 경로에 디렉토리 리스팅이 되는 기능을 하는 웹서버


## CGIHTTPServer
