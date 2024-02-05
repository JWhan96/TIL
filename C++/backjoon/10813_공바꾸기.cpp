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

// #include <iostream>

// using namespace std;

// int main() {
//   int n, m;
//   cin >> n >> m;
//   int a, b;
//   int j, k;
//   int arr[n+1] = {0, };

//   for (int i=1; i<=n; i++){
//     arr[i] = i;
//   }

//   for (int i=1; i<=m; i++){
//     cin >> a >> b;
//     j = arr[a];
//     k = arr[b];
//     arr[a] = k;
//     arr[b] = j;
//   }

//   for (int i=1; i<=n; i++){
//     cout << arr[i] << " ";
//   }

//   return 0;
// }