#include <iostream>

using namespace std;

int main() {
  // c++은 복합데이터형을 제공
  // -> 사용자 정의대로 새로운 데이터형 생성 가능
  // 복합 데이터형 : 기본 정수형과 부동소수점형의 조합

  // 1. 배열(array): 같은 데이터형의 집합
  // typeName arrayName[arraySize]

  // short month[12] = {1, 2, 3}; // 배열 선언

  // cout << month[1] << endl; // 2

  // 배열 원소에 대입할 값들을 콤마로 구분하여 중괄호로 묶어 선언
  // 초기화를 선언 이후 나중에 할 수는 없음
  // 배열을 다른 배열에 통째로 대입 X
  // 초기화 값의 개수를 배열 원소의 개수보다 모자라게 제공 가능
  // 배열을 부분적으로 초기화하면, 나머지 원소들은 모두 0으로 설정
  // 배열을 초기화할 때 대괄호 속을 비워두면 컴파일러가 초기화 값의 개수를 헤아려 배열 원소 개수를 저장
  
  ///////////////////////////////////////////////////

  // 문자열 : 문자의 열
  char a[5] = { 'H', 'e', 'l', 'l', 'o'}; //Hello@jgier
  char b[6] = { 'H', 'e', 'l', 'l', 'o'}; //Hello
  char c[6] = { 'H', 'e', 'l', 'l', 'o', '\0'}; //Hello
  char d[] = { 'H', 'e', 'l', 'l', 'o', '\0'}; //Hello
  char e[] = "Hello"; //Hello

  cout << a << endl << b << endl << c << endl << d <<endl << e << endl;

  return 0;
}