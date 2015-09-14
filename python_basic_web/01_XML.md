# XML

#### XML Python package
- xml.parsers.expat : Fast XML parsing using Expat
- xml.dom : DOM API
- xml.sax : SAX
- xml.etree.ElementTree : The ElementTree XML API

---

### Fast XML parsing using Expat
- 빠른 XML문서파싱이 장점
- xmlparser라는 단하나의 확장 모듈을 제공
- ParserCreate()를 이용해 xmlparser객체를 생성하고, 그 객체로 파싱을 수행
- non-validating 문서의 유효성 검사를 하지 않음
- Event handler : xmlparser사 실행되면서 파싱의 시작, 레리먼트 혹은 문자 데이터발견등의 이벤트가 발생하면 핸들러에 등록된 함수가 호출됨

### DOM API
- 각 성분을 객체로 표현하고 모든객체를 메모리에 저장하고 처리하는 방법
- 애플리케이션에서 XML에 접근할때 밥로 접근할 수 있으며, 연관된 데이터를 연속적으로 참고
- well-formed XML문서는 DOM트리 형태로 표현가능

### SAX(Simple API for XML)
- XML문서를 파싱할때 구성요소를 발견할때마다 이벤트를 발생시켜 XML문서를 처리하는 방법
- Read-Only : DOM과는 다르게 XML문서의 내용을 변경할수 없다.
- Forward : 파싱은 문서의 처음에서 시작해 아래로 진행
- 객체기반방식(DOM) 보다는 빠르지만 한번처리한 문자는 다시 사용할수 없다.
- *이벤트기반 문서처리방식이라고 하며, 보통은 매우 큰 XML문서를 처리할때 많이 사용*

---
### XML Parsing

#### Node

#### Element
