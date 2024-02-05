/// 1. 문자열 이용방법
// #include <iostream>
// #include <string>
// using namespace std;

// int main() {
//     int a, c, result;
//     a = c = result = 0;
//     string b;
//     cin >> a >> b;

//     c = b[2] - '0';
//     cout << a * c << endl;
//     c = b[1] - '0';
//     cout << a * c << endl;
//     c = b[0] - '0';
//     cout << a * c << endl;

//     cout << a * stoi(b);

//     return 0;
// }
////////////////////
// 2. 숫자로만 풀기
#include <iostream>

using namespace std;

int main() {
  int a, b;
  cin >> a >> b;

  cout << a*((b%100)%10) << endl;
  cout << a*((b%100)/10) << endl;
  cout << a*((b/100)) << endl;
  cout << a*b;
  return 0;
}