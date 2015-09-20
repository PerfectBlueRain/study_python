## Web Client Library
- urlparse모듈
- urllib2모듈
- httplib모듈

---

---

#### urlparse모듈
- URL의 분해, 조립, 변경 등을 처리하는 함수를 제공하며, parse한 결과를 리턴
- **urlparse()**함수: ***ParseResult인스턴스*** URL파싱의 결과로
   - 속성값의 의미
      - scheme : URL에 사용된 프로토콜을 의미
      - netloc : 네트워크의 위치, user:password@host:port 형식으로 표현되며, HTTP 프로토콜일 경우 host:port 형식으로 지정된다.
      - path : 파일이나 애플리케이션 경로를 의미
      - params : 애플리케이션에 전달될 매개변수
      - query : 질의 문자열로 앰퍼샌드(&)로 구분된 키=값 쌍 형식으로 표현
      - fragment : 문서내의 앵커 등 조각을 지정
- urlsplit(), urljoin(), parse_qs()

```python
>> from urlparse import urlparse
>> result = urlparse("http://www.python.org:80:80/guido/python.html;philosophy?overall=3#n10")
>> result
ParseResult(scheme='http',
            netloc='www.python.org:80:80',
            path='/guido/python.html',
            params='philosophy',
            query='overall=3',
            fragment='n10')
```
---

#### urllib2모듈
- urllib2 모듈은 주어진 URL에서 데이터를 가져오는 기본 기능을 제공
- urlopen() : 이함수는 2.x버전 urllib.urlopen() 함수는 3.x버전에서는 제거되었고 urllib2.urlopen() 함수를 사용
```python
urlopen(url, data=None, [timeout])
```
   - url에 file을 지정하면 로컬 파일을 열수도 있음
   - 요청방식을 POST로 보내고 싶다면 data 인자에 질의 문자열을 지정해주면 된다.
   - timeout은 응답을 기다리는 타임아웃 시간을 초로 표시


- 예제
   - ex) GET: 네이버 웹서버에 페이지를 읽어서 500 바이트 만큼 출력
   ```python
   from urllib2 import urlopen
   f = urlopen("http://www.naver.com")
   print f.read(500)
   ```
   - ex) POST: 네이버 웹서버에 페이지 500 바이트 만큼 출력
   ```python
   from urllib2 import urlopen
   data = "query=python"
   f = urlopen("http://www.naver.com")
   print f.read(500)
   ```
   - ex) POST 방식 요청을 아래와같은 방식으로도 할수 있다.
   ```python
   import urllib2
   req = urllib2.Request(“http://www.naver.com”)
   req.add_header(“Content-Type”,”text/plain”)
   req.add_data(“query=python”)  #POST method
   f = urllib2.urlopen(req)
   print f.read(300)
   ```

---
#### httplib모듈
- GET, POST이외의 방식으로 요청을 노내거나, 요청해더와 바디사이에 타이머를 두어 시간을 지연시키는 등 urllib2모듈로는 쉽게 처리할수없는 경우,
혹은 HTTP프로토콜 요청에 대한 저수준의 더 세밀한 기능이 필요할때 사용
- HTTPConnection() : 지정된 url 에 대해 HTTPConnection 객체의 인스턴스를 형성하여 반환환

- 예제
   - GET
   ```python
   import httplib﻿
   conn = HTTPConnection('www.naver.com')﻿
   conn.request('GET','/')
   response = conn.getresponse()﻿
   # print response.status
   data = response.read()
   # print response.getheader(header)
   # print response.getheaders﻿()
   conn.close()
   ```

   - POST
   ```python
   import httplib
   conn = httplib.HTTPConnection('www.naver.com')
   conn.requst('POST','/','foo=bar',{'Content-Type':'application/x-www-form-urlencoded'})
   rsp = conn.getresponse()
   conn.close()
   ```

   - HEAD

   - PUT
