#include <iostream>
#include <algorithm>
using namespace std;

int main() {
  int j, k, n, m;
  cin >> n >> m;
  int arr[n];
  for (int i=0; i<n; i++){
    arr[i] = (i+1);
  }
  
  reverse(arr+2-1, arr + 2);
  for (int i = 1; i<=m; i++){
    cin >> j >> k;
    reverse(arr+j-1, arr + k);
  }
  // cout << "\nReversed array: ";
  for (int i = 0; i < n; i++) {
      cout << arr[i] << " ";
  }

  return 0;
}
