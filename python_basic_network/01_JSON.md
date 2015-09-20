# json
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
