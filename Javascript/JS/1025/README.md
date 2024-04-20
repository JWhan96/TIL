# 함수

 - 선언식(function declaration)
 ```JS
    function add (num1, num2) {
        return num1 + num2
    }
 ```
 - 표현식(function expression)
 ```JS
    const sub = function(num1, num2) {
        return num1 + num 2
    }
 ```

 - 함수 표현식 특징
   - 함수 이름이 없는 "익명 함수"를 사용할 수 있음
   - 선언식과 달리 표현식으로 정의한 함수는 호이스팅 되지 않으므로 함수를 정의하기 전에 먼저 사용할 수 없음

  ... | 선언식 | 표현식
 ---------|----------|---------
  특징 | - 익명 함수 사용 불가능 <br> - 호이스팅 있음 | - 익명 함수 사용 가능 <br> - 호이스팅 없음
  기타 | X | 사용 권장

## 매개변수

 1. 기본 함수 매개변수
 2. 나머지 매개변수 ( 가변 인자 )

### 기본 함수 매개변수(Default function parameter)

 - 값이 없거나 undefined가 전달될 경우 이름 붙은 매개변수를 기본값으로 초기화
 ```JS
    const greeting = function (name = "Anonymous") {
        return `Hi ${name}`
    }

    greeting()
 ```

### 나머지 매개변수(Rest parameters)

 - 임의의 수의 인자를 '배열'로 허용하여 가변 인자를 나타내는 방법
 - 작성 규칙
   - 함수 정의 시 나머지 매개변수 하나만 작성할 수 있음
   - 나머지 매개변수는 함수 정의에서 매개변수 마지막에 위치해야 함
 ```JS
    const myFunc = function (param1, param2, ...restParams) {
        return [param1, param2, restParams]
    }
    myFunc(1, 2, 3, 4, 5) // [1, 2, [3, 4, 5]]
    myFunc(1, 2) // [1, 2 []]
 ```

 - 매개변수 개수 > 인자 개수
 - 누락된 인자는 undefined로 할당
 ```JS
    const threeArgs = function (param1, param2, param3) {
        return [param1, param2, param3]
    }

    threeArgs() // [undefined, undefined, undefined]
    threeArgs(1) // [1, undefined, undefined]
    threeArgs(2, 3) // [2, 3, undefined]
```

 - 매개변수 개수 < 인자 개수
 - 초과 입력한 인자는 사용하지 않음
 ```JS
 const noArgs = function () {
    return 0
 }
 noArgs(1, 2, 3) // 0

 const twoArgs = function (param1, param2) {
    return [param1, param2]
 }
 twoArgs(1, 2, 3) // [1, 2]
 ```

## Spread syntax(전개 구문) => "..."

 - 배열이나 문자열과 같이 반복 가능한 항목을 펼치는 것(확장, 전개)
 - 전개 대상에 따라 역할이 다름
   - 배열이나 객체의 요소를 개별적인 값으로 분리하거나 다른 배열이나 객체 요소를 현재 배열이나 객체에 추가하는 등
 1. 함수와의 사용
    1. 함수 호출 시 인자 확장
    2. 나머지 매개변수 (압축)
 ```JS
    function myFunc(x, y, ,z) {
        return x + y + z
    }

    let numbers = [1, 2, 3]

    console.log(myFunc(...numbers)) // 6

    function myFUnc2(x, y, ...restArgs) {
        return [x, y, restArgs]
    }

    console.log(myFunc2(1, 2, 3, 4, 5))
    console.log(myFunc2(1, 2))
 ```
 2. 객체와의 사용 (객체 파트에서 진행)
 3. 배열과의 활용 (배열 파트에서 진행)

## 화살표 함수(arrow function) => 함수 표현식의 간결한 표현법

 1. function 키워드 제거 후 매개변수와 중괄호 사이에 화살표(=>) 작성
 2. 함수의 매개변수가 하나 뿐이라면, 매개변수의 "()" 제거 가능 (단, 생략하지 않는 것을 권장)
 3. 함수 본문의 표현식이 한 줄이라면, "{}" 와 "return" 제거 가능

 - 심화 내용
 ```JS
    // 1. 인자가 없다면 () or _ 로 표시 가능
    const noArgs1 = () => "No args"
    const noArgs2 = () => "No args"

    // 2-1 object를 return 한다면 return 을 명시적으로 작성해야 함
    const returnObject1 = () => { return { key : "value"}}
 ```

## 객체

 - 키로 구분된 데이터 집합을 저장하는 자료형(data collection)
 - 중괄호를 이용해 작성
 - 중괄호 안에 key:value 쌍으로 구석된 속성(property)를 여러 개 작성 가능
 - key는 문자형만 허용
 - value는 모든 자료형 허용
 ```JS
    const user = {
        name: "Alice",
        "key with space": true,
        greeting : function () {
            return "hello"
        }
    }
 ```

 - 속성 참조
   - 점(".", chaining operator) 또는 대괄호([])로 객체 요소 접근
   - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능
   ```JS
    console.log(user.name) // Alice
    console.log(user["key with space"]) // true

    // 추가
    user.address = "korea"
    console.log(user) // {name: "Alice", key with space: true, address: 'kora', greeting: f}
   ```

## Method = > 객체 속성에 정의된 함수

 - object.method() 방식으로 호출
 - 메서드는 객체를 "행동"할 수 있게 함
 ```JS
    console.log(user.greeting()) // hello
 ```

### this

 - 함수나 메서드를 호출한 객체를 가리키는 키워드
 - 함수 내에서 객체의 속성 및 메서드에 접근하기 위해 사용
 - 화살표 함수의 경우 정의한 곳 기준으로 한 단계 상위 스코프의 this 를 참조
 - 가리키는 대상 => 전역 객체
 ```JS
    const person = {
        name : "Alice",
        greeting : function () {
            return `Hello my name is ${this.name}`
        },
    }
    console.log(person.greeting()) // Hello my name is Alice
 ```

 호출 방법 | 대상 
 ---------|----------
  단순 호출 | 전역 객체 
  메서드 호출 | 메서드를 호출한 객체 

 - JavaScript에서 this는 함수가 "호출되는 방식"에 따라 결정되는 현재 객체를 나타냄
 - JavaScript의 함수는 호출될 때 this를 암묵적으로 전달 받음
 - Python의 self와 Java의 this가 선언 시 값이 이미 정해지는 것에 비해 JavaScript의 this는 함수가 호출되기 전까지 값이 할당되지 않고 호출 시에 결정됨(동적 할당)

## 추가 객체 속성

 1. 단축 속성 
    - 키 이름과 값으로 쓰이는 변수의 이름이 같은 경우 단축 구문을 사용 할 수 있음
    ```JS
        const name = "Alice"
        const age = 30

        const user = {
            name: name,
            age: age,
        }
        const user = {
            name,
            age,
        }
    ```
 2. 단축 메서드
    - 메서드 선언 시 function 키워드 생략 가능
    ```JS
        const myObj1 = {
            myFunc : function () {
                return "Hello"
            }
        }

        const myObj2 = {
            myFunc() {
                return "Hello"
            }
        }
    ```
 3. 계산된 속성(computed property name)
    - 키가 대괄호([])로 둘러싸여 있는 속성
    - 고정된 값이 아닌 변수 값을 사용할 수 있음
    ```JS
        const product = prompt("물건 이름을 입력해주세요")
        const prefix = "my"
        const suffix = "property"

        const bag = {
            [product]: 5,
            [prefix + suffix]: "value",
        }

        console.log(bag) // {연필 : 5, myproperty: "value"}
    ```
 4. 구조 분해 할당(destructing assignment)
    - 배열 또는 객체를 분해하여 속성을 변수에 쉽게 할당할 수 있는 문법
    ```JS
        const userInfo = {
            firstName : "Alice",
            userId : "alice123",
            email : "alice123@gmail.com"
        }

        const firstName = userInfo.name
        const userId = userInfo.userId
        const email = userInfo.email

        const {firstName}  = userInfo
        const {firstName, userId} = userInfo
        const {firstName, userId, email} = userInfo
    ```
 5. Object with "전개 구문"
    - 객체 복사
    - 얕은 복사에 활용 가능
    ```JS
        const obj = {b: 2, c: 3, d: 4}
        const newObj = {a: 1, ...obj, e: 5}
        console.log(newObj) // {a: 1, b: 2, c: 3, d: 4, e: 5}
    ```
 6. 유용한 객체 메서드
    - Object.keys()
    - Object.values()
 7. Optional chaining("?.")
    - 속성이 없는 중첩 객체를 에러 없이 접근할 수 있음
    - 만약 참조 대상이 null 또는 undefined라면 에러가 발생하는 것 대신 평가를 멈추고 undefined를 반환
    1. obj?.prop

## JSON

 - JavaScript Object Notation
 - Key-Value 형태로 이루어진 자료 표기법
 - JavaScript의 Object와 유사한 구조를 가지고 있지만 JSON은 형식이 있는 문자열
 - JavaScript에서 JSON을 사용하기 위해서는 Object 자료형으로 변경해야 함

## 참고

### new 연산자

 - JS에서 객체를 하나 생성한다고 하면?
   - 하나의 객체를 선언하여 생성
 - 동일한 행텽의 개게를 또 만든다면?
 - 사용자 정의 객체 타입을 생성
 - 매개변수
    1. constructor : 객체 인스턴스의 타입을 기술하는 함수
    2. arguments : constructor와 함께 호출될 값 목록
 - new constructor[([arguments])]
 ```JS
    function Member(name, age, sId) {
        this.name = name
        this.age = age
        this.sId = sId
    }
    
    const member3 = new Member("Bella", 21, 20226543)
 ```

### JavaScript "this" 장단점

 - this가 미리 정해지지 않고 호출 방식에 의해 결정되는 것은
 - 장점
   - 함수(메서드)를 하나만 만들어 여러 객체에서 재사용할 수 있다는 것
 - 단점
   - 이런 유연함이 실수로 이어질 수 있다는 것

## 배열

 - Object : 키로 구분된 데이터 집합(data collection)을 저장하는 자료형
 - Array : 순서가 있는 데이터 집합을 저장하는 자료구조
 - 배열 구조
   - 대괄호([])를 이용해 작성
   - 배열 요소 자료형 : 제약 없음
   - length 속성을 사용해 배열에 담김 요소가 몇 개인지 알 수 있음

### 메서드

 - push/pop : 배열 끝 요소를 추가 / 제거
 - unshify / shift : 배열 앞 요소를 추가 / 제거

### Array Helper Methods

 - 배열을 순회하며 특정 로직을 수행하는 메서드

메서드 | 역할 
---------|----------
 forEach | 인자로 주어진 함수(콜백함수)를 배열 요소 각각에 대해 실행 
 map | 배열 내의 모든 요소 각각에 대해 함수(콜백함수)를 호출하고, 함수 호출 결과를 모아 새로운 배열을 반환

 - forEach 구조
   - arr.forEach(callback(item[, index[, array]]))
   - 콜백함수는 3가지 매개변수로 구성
    1. item : 처리할 배열의 요소
    2. index : 처리할 배열의 요소 인덱스 (선택 인자)
    3. array : forEach를 호출한 배열 (선택 인자)
   - 반환 값 : undefined

 - 콜백 함수(callback function)
   - 다른 함수에 인자로 전달되는 함수

 - map()
   - 배열 내의 모든 요소 각각에 대해 함수를 호출하고 함수 호출 결과를 모아 새로운 배열을 반환
   - 반환 값이 존재함
   - 새로운 배열을 만들어냄

 
방식 | 특징 | 비고
---------|----------|---------
 for loop | - 배열의 인덱스를 이용하여 각 요소에 접근<br> - break, continue 사용 가능 | X
 for...of | - 배열 요소에 바로 접근 가능 <br> - break, continue 사용 가능 | X
 forEach | - 간결하고 가독성이 높음 <br> - callback 함수를 이용하여 각 요소를 조작하기 용이 <br> - break, continue 사용 불가능 | 사용 권장

### 콜백함수 구조를 사용하는 이유

 1. 함수의 재 사용성 측면
    - 함수를 호출하는 코드에서 콜백 함수의 동작을 자유롭게 변경할 수 있음
    - map 함수는 콜백 함수를 인자로 받아 배열의 각 요소를 순회하며 콜백 함수를 실행
    - 콜백 함수는 각 요소를 변환하는 로직을 담당하므로, map 함수를 호출하는 코드는 간결하고 가독성이 높아짐
 2. 비동기적 처리 측면
    - setTimeout 함수는 콜백 함수를 인자로 받아 일정 시간이 지난 후 실행
    - setTimeout 함수는 비동기적으로 콜백 함수를 실행하므로, 다른 코드의 실행을 방해하지 않음