#include <iostream>
#include <string>

using namespace std;

int main(){
  char alphabet[5][3] = {
    {'A', 'B', 'C'},
    {'A', 'G', 'H'},
    {'H', 'I', 'J'},
    {'K', 'A', 'B'},
    {'A', 'B', 'C'}
  };
  int arr[256] = {0};
  char result;
  string str;
  for (int i=0; i<5; i++){
    for (int j=0; j<3; j++){
      arr[alphabet[i][j]]++;
      // cout << arr[alphabet[i][j]]<<endl;
    }
  }

  for (int i=65; i<100; i++){
    if (arr[i]!=0){
      // cout << arr[i] << endl;
      result = i;
      // cout << result << endl;
      for (int j =0; j<arr[i]; j++){
        cout << result;
      }
    }
    
  }
  return 0;
}