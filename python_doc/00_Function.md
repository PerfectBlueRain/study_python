# Function
- 함수보다 확장된 개념이 module / class
- Lambda함수 / iterator / generator
- def : Function Object(함수객체)를 만드는 구문
- 함수이름은 함수객체의 Reference(레퍼런스)
- > globals() : 생성된 함수 객체를 볼수있다.
- return : 오직한개의 객체만 반환한다. 
           but 한번의 함수호출로 두변수에 값을 각각 할당할수도 있다. 이런경우 정확히 말하면 여러개의 값을 하나의 튜플객체로 만들어 반환하는것
           
- Call by reference : 호출자가 전달하는 변수가 mutable일때와 immutable일때 내부에서 처리하는 방식이 다르다

```{.python}
ex) mutable
> def change(x):
	x[0] = 'H'     // 즉, x[0]은 레퍼런스가 아니라 실제 데이터가 있는 주소를 의미한다.
> wordlist = ['J', 'A', 'M']
> change(wordlist)
> wordlist  // ['H', 'A', 'M'] 즉  변경이 되는 것이다!
```
	
```{.python}
ex) immutable
> def change(x):
	x = x[:]       // 중요한 부분인데 입력받은 인자를 모두 x에 복사한다!
	x[0] = 'H'
	return None
> wordlist = ['J', 'A', 'M']
> change(wordlist)
> wordlist  // ['J', 'A', 'M'] 즉  변경이 안된다! 
```

- Scoping rule
	- namespace
	- LGB(Local / Global / Built-in)
	- global선언문 : 전역변수로 사용하고 싶을때
	- '__builtins__ : 내장영역의 이름이 저장된 리스트 ex) dir(__builtins__)

- function argument
	- 키워드인자
	- 가변인자 리스트 : *
	- 정의되지 않은 인자 처리하기 : **
	
- **Lambda function**
	- 이름이 없고, 함수 객체만 존재하는 익명함수. 
	
---

- iterator
	- 리스트, 튜플, 문자열 처럼 순회가능한 객체에서는 이터래이터라는 특별한 객체가 포함되어있다.
	- 순회가능한 객체의 요소에 순서대로 접근할수있는 객체이다.
	- enumerate() : 순회가능한 객체에서 인덱스 값과 요소의 값을 둘다 반환

```{.python}
> s = 'abc'
> it = iter(s)
> it 
> next(it)
> it.__next__()
```
	
- generators
	- 이터레이터를 만드는 강력한 도구.
	- 함수가 호출되면 지역변수롸 코드가 스택에 적재되고 코드를 실행, 그리고 함수가 끝나면 스택이 사라짐
	- 함수에 return대신에 yield를 적으면 함수를 끝내지 않고 호출한 곳에 값을 전달한다.
	- 리스트 내장에 비해 메모리 절약 측면에서 우수 : 데이터를 미리만들어 놓는 것이아니라 필요할때마다 데이터를 생성 할 수 있어서
