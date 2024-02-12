#include <iostream>

using namespace std;

int main() {
  int arr[9][9] ={};
  int max_result = 0, max_row = 0, max_col = 0;
  for (int i = 0; i<9; i++){
    for (int j = 0; j<9; j++){
      cin >> arr[i][j];
      if (arr[i][j] >= max_result){
        max_result = arr[i][j];
        max_row = i+1;
        max_col = j+1;
      }
    }
  }
  cout << max_result << endl << max_row << " " << max_col;

  
  return 0;
}