#include <iostream>

using namespace std;

int main() {
  int n, m;
  cin >> n >> m;
  int i, j, ball;

  int arr[n+1] = {0, };

  for (int k=1; k<=m; k++){
    cin >> i >> j >> ball;    
    for (int u=i; u<=j; u++){      
      arr[u] = ball;      
    }
  }

  for (int z=1; z<=n; z++){
    cout << arr[z] << " ";
  } 
  return 0;
  }
  

