#include <iostream>
#include <algorithm>

using namespace std;

int main() {
  int arr[28];
  int n = 28;
  int arr2[2];
  int point = 0;
  int target=1;
  for (int i=0; i < n; i++){
    cin >> arr[i];
  }
  sort(arr, arr + 28);
  // for (int i = 0; i < 28; ++i) {
  //     cout << arr[i] << " ";
  // }
  for (int i = 0; i < 30; ++i){    
    if (point == 2){
      break;
    }
    if (arr[i]==target){
      target++;
    }
    else{
      arr2[point]=target;
      point++;
      target++;
      if (arr[i]==target){
        target++;
      }
    }
  }
  for (int i=0; i<2; i++){
    cout << arr2[i] << endl;
  }
  return 0;
}