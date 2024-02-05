# 배열 입력
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

## 배열 뒤집기
- #include <algorithm>
- reverse(arr+start-1, arr + end);

## 인풋, 초기화 틀
- 15552_빠른 A+B 참고

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

