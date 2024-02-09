#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
  int n, cnt;
  cin >> n;
  cnt = 0;
  char arr[n*2+1];
  for (int i =1; i<=(n*2)-1; i++){
    fill(arr , arr + (n*2), ' ');
    if (i<n){
      fill(arr + (n-cnt), arr + (n+cnt+1), '*');
      for (int k =1; k<=(n+cnt); k++){
        cout << arr[k];
      }
      cout << endl;
      cnt++;
    }
    else if (i>=n){
      fill(arr + (n-cnt), arr + (n+cnt+1), '*');
      for (int k =1; k<=(n+cnt); k++){
        cout << arr[k];
      }
      cout << endl;
      cnt--;
    }
  }


  return 0;
}