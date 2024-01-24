#include <iostream> // 전처리 지시자
#include <string>


using namespace std;

int main() {
	// c++ 코드에는 반드시
	// main의 이름을 가지고 있는 함수가 있어야한다
	// ';'이 종결자
	string a = "he안llo";
	cout << a.length() << endl;
	cout <<	"world";

	//endl 줄바꿈
	//<< 데이터의 방향을 나타냄

	// using namespace std; 를 안쓴다면
	// std::cout << "hello" << std::endl;
	// 다음과 같이 항상 std를 붙여주어야한다


	return 0;
}