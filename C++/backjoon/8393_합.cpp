#include <iostream>

using namespace std;

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0); cout.tie(0);

  int n, i, result;
  result = 0;
  cin >> n;
  for ( i =1; i <= n; i++){
    result += i;
  }
  cout << result << endl;

  return 0;
}