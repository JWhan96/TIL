// #include <iostream>
// #include <string>
// using namespace std;

// int main() {
//     string word;
//     cin >> word;
//     cout << word.length() << endl;
//     return 0;
// }

#include <iostream>
using namespace std;

int main() {
    char word[101]; // 최대 길이가 100인 단어를 저장할 배열
    cin >> word;
    int length = 0; // 단어의 길이를 저장할 변수 초기화
    // 배열의 끝을 나타내는 널 문자('\0')가 나올 때까지 반복하여 길이 계산
    while (word[length] != '\0') {
      length++;
    }

    cout << length << endl;
    return 0;
}