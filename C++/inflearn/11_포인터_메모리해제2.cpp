#include <iostream>

using namespace std;

int main(){
  // new연산자
  // 어떤 데이터형을 원하는지 new연산자에게 알려주면,
  // new연산자는 그에 알맞은 크기의 메모리 블록을
  // 찾아내고 그 블록의 주소를 리턴한다.

  // delete 연산자
  // 사용한 메모리를 다시 메모리 폴로 환수
  // 환수된 메모리는 프로그램의 다른 부분이 다시 사용

  // new로 대입하지 않은 메모리는 delete로 해제할 수 없다
  // 같은 메모리 블록을 연달아 두 번 delete로 해제할 수 없다
  // new[]로 메모리를 대입할 경우 delete[]로 해제한다
  // 대괄호를 사용하지 않았다면 delete도 대괄호를 사용하지 않아야함
  double* p3 = new double[3]; // double형 데이터 3개를 저장할 수 있는 공간을 대입
  p3[0] = 0.2; // p3를 배열 이름처럼 취급
  p3[1] = 0.5;
  p3[2] = 0.8;

  cout << "p3[1] is " << p3[1] << ".\n";

  p3 = p3 + 1;

  cout << "Now p3[0] is " << p3[0] << " and ";
  cout << "p3[1] is " << p3[1] << "\n.";

  p3 = p3-1;
  delete[] p3;

  return 0;
}