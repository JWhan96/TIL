#include <iostream>
#include <string>

using namespace std;

int main(){
  string vect = "MINCODING";
  int n;
  cin >> n;
  int arr[256] = {0};
  char str;
  for (int i=0; vect[i]; i++){
    arr[vect[i]]++;
  }
  for (int i =0; i<n; i++){
    cin >> str;
    if(arr[str] != 0){
      cout << 'O';  
    }
    else{
      cout << 'X';
    }
  }

  return 0;
}