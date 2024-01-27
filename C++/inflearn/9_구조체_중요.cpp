#include <iostream>
#include <cstring>

using namespace std;

int main(){
  // 구조체: 다른 데이터형이 허용되는 데이터의 집합
  // cf) 배열: 같은 데이터형의 집합
    struct MyStruct {
        string name;
        string position;
        int height;
        int weight;
    } B;

    MyStruct A;
    // 구조체의 멤버연산자 .
    A.name = "Son";
    A.position = "Striker";
    A.height = 183;
    A.weight = 77;
    /*
    MyStruct A = {
        "Son",
        "Striker",
        183,
        77
    }
    */
    cout << A.name << endl;
    cout << A.position << endl;
    cout << A.height << endl;
    cout << A.weight << endl;

    B = {

    };
    // 선언한 구조체로 자동으로 할당
    cout << B.height << endl;

    MyStruct C[2] = {
        {"A", "A", 139, 1},
        {"B", "B", 2, 2}
    };

    cout << C[0].height << endl;

    return 0;
}