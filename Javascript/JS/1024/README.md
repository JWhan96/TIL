# Basic Syntax

 1. 변수
 2. 데이터 타입
 3. 연산자
 4. 조건문
 5. 반복문

## 변수

 - 반드시 문자, 달러($) 또는 밑줄(_)로 시작
 - 대소문자를 구분
 - 예약어 사용 불가(for, if, function)
 - 카멜 케이스(camelCase) : 변수, 객체, 함수에 사용
 - 파스칼 케이스(PascalCase) : 클래스, 생성자에 사용
 - 대문자 스네이크 케이스(SNAKE_CASE) : 상수(constants)에 사용

### 변수 선언 키워드

 - 블록 스코프(block scope)
   - if, for, 함수 등의 중괄호({}) 내부를 가리킴
   - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

    ```JS
        let x = 1
        if (x == 1) {
            let x = 2
            console.log(x) // 2
        }
        console.log(x) // 1
    ```

 1. let
    - 블록 스코프(block scope)를 갖는 지역 변수를 선언
    - 재할당 가능
    - 재선언 불가능
 2. const
    - 블록 스코프를 갖는 지역 변수 선언
    - 재할당 불가능
    - 재선언 불가능
 3. var
    - 재할당 가능 & 재선언 가능
    - "호이스팅"되는 특성으로 인해 예기치 못한 문제 발생 가능
    - 함수 스코프(function scope)를 가짐
    - 변수 선언 시 var, const, let 키워드 중 하나를 사용하지 않으면 자동으로 var로 선언됨

## 데이터 타입

 - 원시 자료형(Primitive type) : Number ,String, Boolean, undefined, null
 - 참조 자료형(Reference type) : Object, Array, Function)

### 원시 자료형

 - 변수에 할당될 때 값이 복사됨

 ```JS
    const bar = "bar";
    console.log(bar); // bar

    bar.toUpperCase()
    console.log(bar) // bar
 ```

 - Number : 정수 또는 실수형 숫자를 표현하는 자료형
   ```JS
      const a = 13
      const b = -5
      const c = 3.14 // float - 숫자표현
      const d = 2.998e8 // 2.998 * 10^8 = 299,800,000
      const e = Infinity
      const f = -Infinity
      const g = NaN // Not a Number
   ```

 - String : 텍스트 데이터를 표현하는 자료형
   - "+" 연산자를 사용해 문자열끼리 결합
   - 곱셈, 나눗셈, 뺄셈 불가능
   ```JS
      const firstName = "Tony";
      const lastName = "Stark";
      const fullName = firstName + lastName;
      console.log(fullName) // TonyStark
   ```

 - Template literals(템플릿 리터럴)
   - 내장된 표현식을 허용하는 문자열 작성 방식
   - Backtick(``)을 이용하며, 여러 줄에 걸쳐 문자열을 정의할 수도 있고 JavaScript의 변수를 문자열 안에 바로 연결할 수 있음
   - 표현식은 '$'와 중괄호(${expression})로 표기

 - null : 변수의 값이 없음을 의도적으로 표현할 때 사용
 - undefined : 변수 선언 이후 직접 값을 할당하지 않으면 자동으로 할당됨

 - '값이 없음'에 대한 표현이 null과 undefined 2가지인 이유
   - JavaScript의 설계 실수
   - null이 원시 자료형 임에도 불구하고 object로 출력되는 이유는 JavaScript 설계 당시의 버그를 해결하지 않은 것

 - Boolean(true/false) : 조건문 또는 반복문에서 Boolean이 아닌 데이터 타입은 "자동 형변환 규칙"에 따라 true or false로 변환됨

    데이터 타입 | false | true
   ---------|----------|---------
    undefined | 항상 false | X
    null | 항상 false | X
    Number | 0, -0, NaN | 나머지 모든 경우
    String | 빈 문자열 | 나머지 모든 경우

## 연산자

 - 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
 - 단축 연산자 지원

### 증가 & 감소 연산자

 - 증가 연산자(++)
   - 피연산자를 증가(1을 더함)시키고 연산자의 위치에 따라 증가하기 전이나 후의 값을 반환

 - 감소 연산자(--)
   - 피연산자를 감소(1을뻄)시키고 연산자의 위치에 따라 감소하기 전이나 후의 값을 반환

 - += 또는 -= 와 같이 더 명시적인 표현으로 작성 하는 것을 권장

 - 비교 연산자 : 피연산자들(숫자, 문자, Boolean 등)을 비교하고 결과 값을 boolean으로 변환하는 연산자

 - 동등 연산자(==)
   - 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
   - '암묵적 타입 변환' 통해 타입을 일치시킨 후 같은 값인지 비교
   - 두 피연산자가 모두 객체일 경우 메모리의 같은 객체를 바라보는지 판별

 - 일치 연산자(===)
   - 두 피연산자의 값과 타입이 모두 같은 경우 true를 반환
   - 같은 객체를 가리키거나, 같은 타입이면서 같은 값인지를 비교
   - 엄격한 비교가 이뤄지며 암묵적 타입 변환이 발생하지 않음
   - 특수한 경우를 제외하고는 동등 연산자가 아닌 일치 연산자 사용 권장

## 조건문

 - 조건 표현식의 결과값을 boolean 타입으로 변호나 후 참/거짓을 판단

 ```JS
   const name = "customer"

   if ( name == "admin" ) {
      console.log("관리자님 환영해요")
   } else if ( name === "customer" ) {
      console.log("고객님 환영해요")
   } else {
      console.log(`반갑습니다. ${name}님`)
   }
 ```

 - 조건 (삼항) 연산자
   - 세 개의 피연산자를 받는 유일한 연산자
   - 앞에서부터 조건문, 물음표(?), 조건문이 참일 경우 실행할 표현식, 콜론(:), 조건문이 거짓일 경우 실행할 표현식이 배치
   ```JS
      person > 17 ? "Yes" : "No"
   ```

## 반복문

 - while
 - for
 - for...in
 - for...of

### while

 - 조건문이 참이면 문장을 계속해서 수행

 ```JS
   let i = 0

   while (i < 6>) {
      console.log(i)
      i += 1
   }
 ```

### for

 - 특정한 조건이 거짓으로 판별될 때까지 반복
 ```JS
   for (let i = 0; i < 6; i++) {
      console.log(i)
   }
 ```

### for...in

 - 객체의 열거 가능한 속성(property)에 대해 반복
 ```JS
   const fruits = { a: 'apple', b: 'banana'}
   for (const fruit in fruits) {
      console.log(fruit) // a, b
      console.log(fruits[fruit]) // apple, banana
   }
 ```

 - 배열의 인덱스는 정수 이름을 가진 열거 가능한 속성
 - for...in은 정수가 아닌 이름과 속성을 포함하여 열거 가능한 모든 속성을 반환
 - 내부적으로 for...in은 배열의 반복자 대신 속성 열거를 사용하기 때문에 특정 순서에 따라 인덱스를 반환하는 것을 보장할 수 없음

### for...of

 - 반복 가능한 객체(배열, 문자열 등)에 대해 반복
 ```JS
   const numbers = [0, 1, 2, 3]

   for (const number of numbers) {
      console.log(number) // 0, 1, 2, 3
   }
 ```

### 반복문 사용시 const 사용 여부

 - for 문
   - for (let i = 0; i < arr.legth; i++) {...} 의 경우 최초 정의한 i를 "재할당" 하면서 사용하기 때문에 const를 사용하면 에러 발생

 - for...in, for...of 
   - 재할당이 아니라, 매 반복마다 다른 속성 이름이 변수에 지정되는 것이므로 const를 사용해도 에러가 발생하지 않음
   - 단, const 특징에 따라 블록 내부에서 변수를 수정할 수 없음

### 반복문 종합

 키워드 | 연관 키워드 | 스코프
 ---------|----------|---------
  while | break, continue | 블록 스코프
  for | break, continue | 블록 스코프
  for...in | object 순회 | 블록 스코프
  for...of | Iterable 순회 | 블록 스코프

### 세미콜론(semicolon)

 - 자바스크립트는 세미콜론을 선택적으로 사용 가능
 - 세미콜론이 없으면 ASI에 의해 자동으로 세미콜론이 삽입됨
   - ASI(Automatic Semicolon Insertion, 자동 세미콜론 삽입 규칙)
 - JavaScript를 만든 Brendan Eich 또한 세미콜론 작성을 반대

### 함수 스코프(function scope)

 - 함수의 중괄호 내부를 가리킴
 - 함수 스코프를 가지는 변수는 함수 바깥에서 접근 불가능

### 호이스팅(hoisting)

 - 변수를 선언 이전에 참조할 수 있는 현상
 - 변수 선언 이전의 위치에서 접근 시 undefined를 반환
 - JavaScript에서 변수들은 실제 실행시에 코드의 최상단으로 끌어 올려지게 되며 (hoisted) 이러한 이유 때문에 var로 선언된 변수는 선언 시에 undefined 로 값이 초기화되는 과정이 동시에 발생

 ```JS
   console.log(name) // undefined => 선언 이전에 참조
   
   var name = "홍길동" // 선언

   // 위 코드를 암묵적으로 아래와 같이 이해함
   var name
   console.log(name)

   var name = "홍길동"
 ```

### NaN을 반환하는 경우 예시

 1. 숫자로서 읽을 수 없음 (Number(undefined))
 2. 결과가 허수인 수학 계산식(Math.sqrt(-1))
 3. 피연산자가 NaN (7**NaN)
 4. 정의할 수 없는 계산식(0*Infinity)
 5. 문자열을 포함하면서 덧셈이 아닌 계산식("가"/3)