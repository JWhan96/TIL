#include <iostream>

using namespace std;

int main() {
  // 공용체(union)
  // 서로 다른 데이터형을 한 번에 한가지만 보관할 수 있음
  // 다른 데이터값을 보관할 때 마다 이전의 데이터값 소실
  // 장점: 메모리 저장에서 이득
  union Myunion
  {
    int intVal;
    long longVal;
    float floatVal;
  };

  Myunion test;
  test.intVal = 3;
  cout << test.intVal << endl;
  test.longVal = 33;
  cout << test.intVal << endl;
  cout << test.longVal << endl;
  test.floatVal = 3.3;
  cout << test.intVal << endl;
  cout << test.longVal << endl;
  cout << test.floatVal << endl;

  return 0;
}