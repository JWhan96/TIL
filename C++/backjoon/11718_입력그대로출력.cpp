#include <iostream>
#include <string>
using namespace std;

int main() {
  string a; // 문자열로 변경
  while (getline(cin, a)) { // 문자열로 한 줄씩 입력 받음
    cout << a << endl; // 개행문자를 포함하여 출력
  }
  return 0;
}