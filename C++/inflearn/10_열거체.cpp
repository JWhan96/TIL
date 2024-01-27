#include <iostream>

using namespace std;

int main() {
  // 열거체(enum)
  // 기호 상수를 만드는 것에 대한 또 다른 방법

  enum spectrum { red = 0, orange = 2, yellow = 4, green, blue, violet, indigo, ultraviolet };

  // 1. spectrum을 새로운 데이터형 이름으로 만든다
  // 2. red, orange, .... 0에서부터 7까지 정수 값을 각각 나타내는 기호 상수로 만든다(아무런 옵션을 주지않았을때)
  // 열거자들을 정수값으로 할당 가능하고 따로 언급하지 않는다면 가장 마지막 할당한 다음 정수로 주어진다.
  spectrum a = yellow;
  // spectrum a = yellow + blue; // 열거자들끼리의 산술 값은 불가
  
  cout << a << endl;
  
  // 하지만 열거자들을 인트값에다 대입하면 상수로써 작용

  int b;
  b = blue;
  b = blue + 3;

  cout << b;
  return 0;
}