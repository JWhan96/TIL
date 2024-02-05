#include <iostream>

using namespace std;

int main() {
  int n;
  double maxN, result;
  cin >> n;
  maxN = result = 0;
  int a[n];

  for (int i = 0; i < n; i++) {
    cin >> a[i];
    if (maxN <= a[i]){
      maxN = a[i];
    }
  }
  for (int i = 0; i < n; i++) {       
    result += (a[i]/maxN)*100;
  }
  cout << result/n;

  return 0;
}