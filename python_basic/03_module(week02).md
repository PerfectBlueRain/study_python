# Module & Package


## Module
- 함수나 변수들, 또는 클래스들을 모아놓은 파일
- 별도의 namespace제공
- 모듈의 종류 : 표준 모듈 / 사용자 생성 모듈 / 써드 파티 모듈
- 모듈의 사용 
	- import 모듈이름 as 애칭
	- 선택적 import
```
from spam import foo
from spam import foo, bar
from spam import (foo, bar, Spam)
from spam import *   =>  __all__ = [‘bar’,’Spam’]
```

```{.python}
코드 중간에 모듈 import
if format == 'xml':
	import xmlreader as reader
elif format == 'csv':
	import csvreader as reader
data = reader.read_data(filename)
```

```{.python}
모듈 검색 경로
import sys 
sys.path.append("mymodules.zip") 
import foo, bar
```

## Package
- 모듈을 공통의 이름으로 묶는데 사용
- 도트('.')를 이용하여 파이썬 모듈을 계층적(디렉토리 구조)으로 관리
- __init__.py
	- import * =>  __all__ = ['모듈이름1', '모듈이름2', ...]
	
- 상대적 import
	- from . import lines : 폴더안의 모듈
	- from ..P
	
	
## 배포
- distutils모듈사용
```
python setup. sdist
python setup.py install
```
- setup()의 매개변수

name : 패키지 이름 (필수)
version : 버전번호(필수)
author : 저자이름
author_email : 저자 이메일
maintainer : 관리자 이름
maintainer_email : 관리자 이메일
url : 패키지 홈페이지
description : 패키지에 대한 짧은 설명
download_url : 패키지를 다운로드할 수 있는 위치
classifiers : 문자열 분류자 목록
```{.python}
# setup.py
from distutils.core import setup 
setup(name = "spam",
	  version = "1.0", 
	  py_modules = ['libspam'], 
	  packages = ['spampkg'], 
	  scripts = ['runspam.py'], )
```
