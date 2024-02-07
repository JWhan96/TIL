## 입력 방법
```c++
// 입력 = Hello World!
cin >> a;
cout << a;
//출력 = Hello
```

```c++
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
```
```c++
#include <iostream>
#include <string>

using namespace std;

int main() {
  int n, b;  
  cin >> n;  //cin >> n 코드가 버퍼에 개행 문자('\n')을 남겨둠
  cin.ignore(); // cin.ignore() 함수를 사용하여 버퍼를 비워주는 것
  string a;
  while (getline(cin, a)){
    b = a.length();
    cout << a[0] << a[b-1] << endl;
  }
  return 0;
}
```
참고- [c++입력받기](https://knowable.tistory.com/24)

## 배열 입력
- 입력: 3 40 80 60
- char[]
  ```c++
    int n;
    cin >> n;
    char a[n];
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    cout << a[0] << endl;
    cout << a[1] << endl;
    cout << a[2] << endl;
    // 출력 4 0 8
  ```
- int[]
  ```c++
    int n;
    cin >> n;
    int a[n];
    for (int i = 0; i < n; i++) {
      cin >> a[i];
    }
    cout << a[0] << endl;
    cout << a[1] << endl;
    cout << a[2] << endl;
    // 출력 40 80 60
  ```
## for 문의 2가지 방법
```c++
#include <iostream>
#include <string>

string word;
int n;
for (char ch : word){
  '범위 기반 for 루프-각 문자를 순회'
} 
for (int i=0; i<=n; i++){
  '원하는 값까지 인덱스 순회'
}
```

## 배열 뒤집기
- #include <algorithm>
- reverse(arr+start-1, arr + end);

## 문자열 뒤집기 and 문자열 숫자로 바꾸기
```c++
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
  string a, b;
  cin >> a >> b;
  
  reverse(a.begin(), a.end()); // reverse(a[0], a[-1]) 와 같이 이용하면 안 된다
  reverse(b.begin(), b.end());
  
  cout << max(stoi(a), stoi(b)); // 문자열을 정수로 바꿔주는 메서드(string include해야함)

  return 0;

}
```

## 인풋, 초기화 틀
- 15552_빠른 A+B 참고

## A~Z까지 배열 만들기(아스키코드 이용)
```c++
char arr1[26]; // 26개의 알파벳 + 널 문자('\0')을 포함하여 크기를 27로 설정 
for (int i = 0; i < 26; i++) {
  arr1[i] = 'A' + i; // 알파벳 순서대로 배열에 저장(A=65)
}
```

## 위치바꾸기(swap)
```c++
#include <iostream>
#include <vector>

using namespace std;

int main() {
    int N, M;
    cin >> N >> M;

    // 바구니 초기 상태 생성
    vector<int> baskets(N);
    for (int i = 0; i < N; ++i) {
        baskets[i] = i + 1; // 바구니에 들어있는 공의 초기 번호 설정
    }

    // 공을 교환하는 방법에 따라 바구니의 순서 변경
    for (int m = 0; m < M; ++m) {
        int i, j;
        cin >> i >> j;

        // i번 바구니와 j번 바구니의 위치 교환
        swap(baskets[i - 1], baskets[j - 1]);
    }

    // 바구니에 들어있는 공의 번호 출력
    for (int i = 0; i < N; ++i) {
        cout << baskets[i] << " ";
    }

    return 0;
}
```
## 정렬(sort)
5597_과제안낸사람 참고

## vector and map
```c++
#include <iostream>
#include <vector>
#include <map>

using namespace std;

int main() {
    // 벡터 안에 맵을 담는 예제
    vector<map<string, int>> listOfDictionaries;

    // 맵 생성 및 초기화
    map<string, int> dictionary1 = {{"key1", 1}, {"key2", 2}};
    map<string, int> dictionary2 = {{"key3", 3}, {"key4", 4}};

    // 벡터에 맵 추가
    listOfDictionaries.push_back(dictionary1);
    listOfDictionaries.push_back(dictionary2);

    // 벡터의 내용 출력
    for (const auto& dictionary : listOfDictionaries) {
        for (const auto& pair : dictionary) {
            cout << "{" << pair.first << ": " << pair.second << "} ";
        }
        cout << endl;
    }

    return 0;
}
```

