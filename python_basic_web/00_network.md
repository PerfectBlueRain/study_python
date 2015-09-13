# Python Internet

#### module
- socket
- email
- json
- mailbox
- webbrowser
- urllib
- cgi
- http.client & http.server
- ftp
- xml-rpc

---

### socket
- low레벨의 네트워킹 인터페이스.

```{.python}
################# Server ####################
import socket

HOST = ''
PORT =  50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

connection, address = s.accept()
print('connected by', address)

while True:
    data = connection.recv(1024)
    if not data:
        break
    recvData = "[server response] "+data
    connection.send(recvData)

connection.close()
```


```{.python}
################# Client ####################
import socket

HOST = '127.0.0.1'
PORT = 50007

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(b'Hello, python')
data = s.recv(1024)

s.close()
print('Received', repr(data))
```

### email

### json
- JSON형태의 데이터교환을 위해
- **dump** : python데이터 -> json형태로
- **decode** : json객체를 -> python데이터

```{.python}
#data, data2, data3  비교형식으로 작성함
>>> import json
>>> data = {1:'a',2:'b'}  
>>> data2 = json.dumps(data)
>>> data3 = json.loads(data2)
>>> type(data)
<type 'dict'>
>>> type(data2)
<type 'str'>
>>> type(data3)
<type 'dict'>
>>> print data
{1: 'a', 2: 'b'}
>>> print data2
{"1": "a", "2": "b"}
>>> print data3
{u'1': u'a', u'2': u'b'}
```
- json파싱

```{.python}
config.json
{
      "snapshot" : {
		"repos" : "mingnewbie.tistory.com/repositories/snapshots",
		"userid" : "mingnewbie",
		"passwd" : "1234"
	},
	"release" : {
		"repos" : "mingnewbie.tistory.com/repositories/release",
		"userid" : "mingnewbie",
		"passwd" : "5678"
	},
	"component" : {
		"test":"mingnewbie.tistory.com"
	}
}

import json

CONFIG_FILE="./config.json"
CONFIG={}

def readConfig(filename) :
    f = open(filename, 'r')
    js = json.loads(f.read())
    f.close()
    return js

def main() :
    global CONFIG_FILE
    global CONFIG
    CONFIG = readConfig(CONFIG_FILE)

    repos = CONFIG['snapshot']['repos']
    userid = CONFIG['snapshot']['userid']
    pw = CONFIG['snapshot']['passwd']

    print "repos value : " + repos
    print "userid value : " + userid
    print "pw value : " + pw

if __name__ == "__main__":
    main()
```

### mailbox
- 메일박스를 관리하는데 사용하수있는 모듈

### webbrowser
- 웹브라우저를 간단하게 제어할때 사용

### urllib
- URL과 관련된 패키지. URL파싱, URL에 할당된 데이터를 가져오는 수집까지 여러가지 기능제공

### cgi

### http.client & http.server

### ftp

### xml-rpc
