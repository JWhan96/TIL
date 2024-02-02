#include <iostream>

using namespace std;

int a, b, result;

void init() {
  a = b = 0;
}

void input() {
  cin >> a >> b;
}

void sol() {
  result = a + b;
}

int main() {
  ios::sync_with_stdio(0);  
  cin.tie(0);

  int T;
  int tc;
  cin >> T;
  for (tc=1; tc <= T; tc++) {
    init();
    input();
    sol();
    cout << result << "\n";
  }
  
  return 0;

}
