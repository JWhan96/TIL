# JavaScript

 - 웹 페이지의 "동적인 기능"을 구현하기 위해 사용되는 프로그래밍 언어
 - 초기에는 브라우저에서 실행되어 웹 페이지를 변환시키기 위해서만 사용
 - 서버 측에서도 자바스크립트 실행 환경이 필요해짐
   - 자바스크립트의 강점(비동기 프로그래밍)을 살려서 개발 가능

 - 컴파일 vs 인터프리터
   - 인터프리터 언어에 속함
   - 스크립트 언어
     - 기존에 존재하는 소프트웨어를 제어하기 위한 용도로 쓰이는 언어
     - 연극의 대본(Scrit)이 연기자를 제어하는 것에서 따온 말

 - 메모리 관리 방식
   - 데이터의 타입이 런타임(실행 중)에 결정되는 동적 언어
   - 타입 에러를 개발자가 신경써주어야 한다.

 - ECMAScript : Ecma International이 정의하고 있는 표준화된 스크립트 프로그래밍 언어 명세
 - ECMAScript 와 JavScript
   - JavaScript는 ECMAScript 표준을 구현한 구체적인 프로그래밍 언어
   - ECMAScript의 명세를 기반으로 하여 웹 브라우저나 Node.js 같은 환경에서 실행됨

## DOM

 - HTML 문서를 자바스크립트가 접근 및 조작할 수 있도록 도와주는 API
   - 해당 문서의 요소(Element), 속성(Attribute), 스타일(Style) 등을 접근하고 조작할 수 있도록 트리 형태의 객체 모델로 변환함
 - 즉, DOM은 웹 페이지의 컨텐츠에 대한 프로그래밍 인터페이스를 제공하여, 웹 페이지의 구조를 변경하거나 내용을 동적으로 조작하는 데 사용
 - 웹 브라우저에서 JavaScript : 웹 페이지의 동적인 기능을 구현
 - 웹 페이지(Document)를 구조화된 객체로 제공하여 프로그래밍 언어가 페이지 구조에 접근할 수 있는 방법을 제공

### DOM 선택

 - document.querySelector(selector) => 요소 한 개 선택
   - 제공한 선택자와 일치하는 element 한 개 선택
   - 첫 번째 element 객체를 반환 (없다면 null 반환)

 - document.querySelectorAll(selector) => 요소 여러 개 선택
   - 제공한 선택자와 일치하는 여러 element를 선택
   - 제공한 selector을 만족하는 NodeList를 반환

 - Selector => class : . / id : # / tag : div, p, h3 ...

### DOM 조작

 - 클래스 속성 조작
   - "classList" property => 클래스 목록을 DOMTokenList(유사 배열) 형태로 반환
   - element.classList.add() : 지정한 클래스 값을 추가
   - element.classList.remove() : 지정한 클래스 값을 제거
   - element.classList.toggle() : 클래스가 존재한다면 제거하고 false 반환 존재하지 않으면 추가하고 true 반환

 - 속성 조작 메서드
   - Element.getAttribute() : 해당 요소에 지정된 값을 반환 (조회)
   - Element.setAttribute(name, value) : 지정된 요소의 속성 값을 설정, 이미 있으면 기존 값을 갱신
   - Element.removeAttribute() : 요소에서 지정된 이름을 가진 속성 제거

### DOM 요소 소작 메서드

 - 'textContent' property => 요소의 텍스트 컨텐츠를 표현
 - document.createElement(tagName) : 작성한 tagName의 HTML 요소를 생성하여 반환
 - Node.appendChild() : 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입, 추가된 Node 객체를 반환
 - Node.removeChild() : DOM에서 자식 Node를 제거, 제거된 Node 반환

### style 조작

 - "style" property => 해당 요소의 모든 style 속성 목록을 포함하는 속성

## Node

 - DOM의 기본 구성 단위
 - DOM 트리의 각 부분은 Node 라는 객체로 표현됨
   - Document Node => HTML 문서 전체를 나타내는 노드
   - Element Node => HTML 요소를 나타내는 노드 ex) <p>
   - Text Node => HTML 텍스트, Element Node 내의 텍스트 컨텐츠를 나타냄
   - Attribute Node => HTML 요소의 속성을 나타내는 노드

## NodeList

 - DOM 메서드를 사용해 선택한 Node의 목록
 - 배열과 유사한 구조를 가짐
 - Index로만 각 항목에 접근 가능
 - 다양한 배열 메서드 사용 가능
 - querySelectorAll()에 의해 반환되는 NodeList는 DOM의 변경사항을 실시간으로 반영하지 않음

## Element

 - Node의 하위 유형
 - Element는 DOM 트리에서 