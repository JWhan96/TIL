#include <iostream>

using namespace std;

int main(){
    // C++에서 문자열을 다루는 방법 중 하나인 string
    // C스타일로 string객체를 초기화할 수 있다
    // cin을 사용하여 string객체에 키보드 입력을 저장가능
    // cout을 사용하여 string객체 출력가능
    // 배열 포기를 사용하여 string객체에 저장되어 있는 개별적이 문자들에 접근 가능

    // 배열을 다른 배열에 통재로 대입 불가
    // >> string에서는 가능

    char char1[20];
    char char2[20] = "jaguar";
    string str1;
    string str2 = "panda";
    // char1 = char2; //대입불가
    str1 = str2; // 대입가능
    cout << str1 << str2[0] << endl;
    return 0;
}