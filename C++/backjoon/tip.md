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