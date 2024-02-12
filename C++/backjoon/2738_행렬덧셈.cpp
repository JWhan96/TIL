#include <iostream>

using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  int arr1[n][m];
  int arr2[n][m];
  for (int i=0; i<n; i++){
    for (int j=0; j<m; j++){
      cin >> arr1[i][j];
    }
  }
  for (int k=0; k<n; k++){
    for (int q=0; q<m; q++){
      cin >> arr2[k][q];
  }
  }
  for (int h=0; h<n; h++){
    for (int w=0; w<m; w++){
      cout << arr1[h][w] + arr2[h][w] << " ";
  }
  cout << endl;
  }

  return 0;
}