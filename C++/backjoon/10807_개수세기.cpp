#include <iostream>

using namespace std;

int main() {
  int n, target;
  int result = 0;
  cin >> n;
  int arr[n];
  // int arr2[n] = {0, };
  for (int i=1; i<=n; i++){
    cin >> arr[i];
    // arr2[arr[i]] += 1;

  }
  cin >> target;
  for (int i=1; i<=n; i++){
    if (arr[i]==target){
      result += 1;
    }
  }
  cout << result;

  return 0;
}