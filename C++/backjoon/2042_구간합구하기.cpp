#include <iostream>
#include <algorithm>
#include <numeric>
using namespace std;


int main() {
  long long n, m, k;
  long long a;
  long long b;
  long long c;
  
  cin >> n >> m >> k;
  long long arr[n];
  for (long long i=1; i<=n; i++){
    cin >> arr[i];
  }
  for (long long j =0; j<(m+k); j++){
    long long result = 0;
    cin >> a >> b >> c;
    if (a==1){
      arr[b] = c;
    }
    else if (a==2){
      result = accumulate(arr + b, arr + c+1, 0);
      cout << result << endl;
    }
    
  }

  return 0;
}