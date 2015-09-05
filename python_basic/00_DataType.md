# Data Type

- 자료형
    - list : ['A','B',..] 여러종류의 값을 담을 수 있고, 인덱스가 있고, 슬라이싱이 가능
        - +연산자제공
        - .append('A'), .insert(1, 'B'), .extend(['A', 'B']), index()
        - pop(), count(), remove(), sort(), reverse()
        
    - set : {A, B, C, } 순서가 없다
        - 차집합(-), 교집합(&), 합집합(|) 연산자제공 
        - union(), intersection()
        
    - tuple : ( A, B, C, ) 리스트와 유사하지만 **읽기전용!**, 그만큼 제공되는 함수는 적어도 속도는 빠르다.
        - count(), index()
        - **파이썬내부에서는 튜플을 알게 모르게 사용하는 부분이 많다. 여러값을 다중할당하는 것에도 튜플이 생략되어있다.**
         
         ```{.python}
            > a, b = 1, 2 
            > a, b = b, a  // swap
            > print(a, b)  
         ```
    - dictionary : key&value쌍으로 구성
        - dict()생성자
        - items():모든 키와 값을 tuple로 묶어서 반환 / keys(), values()
        - 삭제 : del문(하나씩) / clear() (전체삭제)

    - bool : True / False를 나타냄

    - 얖은복사 &깊은복사  : copy() / deepcopy()
     
          