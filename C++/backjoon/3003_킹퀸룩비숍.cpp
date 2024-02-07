#include <iostream>
#include <string>

using namespace std;

int main() {
  int arr[6] = {1, 1, 2, 2, 2, 8};
  int arr2[6];

  for (int i=0; i<6; i++){
    cin >> arr2[i];
    cout << arr[i]-arr2[i] << " " ;
  }


  return 0;
}