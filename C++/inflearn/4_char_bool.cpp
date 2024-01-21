#include <iostream>

using namespace std;

int main() {
  // // char : 작은 문자형
  // int a = 77;
  // char b = a;
  // char c = 'a';
  // // char d = "a";
  // // c++에서 char형은 ""는 불가
  // // 이유는 null문자 때문
  // // c++에서는 null문자 '\0'을 만나기 전까지 문자열을 계속 출력하게 됌
  // // "" >> 명시적으로 null문자가 포함 => string
  // cout << b << c << endl;

  // bool : 0 혹은 1 (false, true) => 0이외의 모든 수는 true로 저장
  bool a = 0;
  bool b = 1;
  bool c = 10;

  cout << a << " " << b << " " << c << endl;
  
  return 0;

}