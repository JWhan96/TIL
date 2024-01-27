#include <iostream>

using namespace std;

int main() {
	// 1. 변수란? 변할 수 있는 수
	// cf) 상수 : 변할 수 있는 수

	// 1. 변수의 자료형
	// 2. 변수의 이름
	// 3. 변수가 어디에 저장되는가 (메모리 영역)
	// &를 통해 주소확인 가능(자동으로 컴파일러가 해줌)
	int a;
	a = 7;

	int b = 3;

	a = 5;
	b = 5;

	// 변수는 사용되기 이전에 정의 되어야 한다.
	cout << "a = " << a << "주소:" << & a << endl << "b = " << b << endl;

	/*
	1. 숫자로 시작할 수 없다
	2. c++에서 사용하고 있는 키워드는 사용할 수 없다.
	3. white space를 사용할 수 없음
	*/
	// 잘못된 예
	 //1. int 77aaa;
	 //2. int return;
	 //3. int aa aa;

	return 0;
}