#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main() { 
  int n;
  int len, cnt;
  len = cnt = 0;
  string a;
  // vector<char> arr;
  cin >> n;
  for (int i=0; i<n; i++){
    vector<char> arr;
    cin >> a;
    len = a.length();
    for (int i=0; i<=len; i++){
      if (i==len){
        cnt ++;
        break;
      }
      if (i==0){
        arr.push_back(a[i]);
        // for (int k=0; k<arr.size(); k++){
        //   cout << "arr[k] = " << arr[k] << endl;
        // }
        continue;
      }
      else{
        auto it = find(arr.begin(), arr.end(), a[i]);
        if (it != arr.end()) {
          // 원소를 찾은 경우
          if (a[i]==a[i-1]){
            continue;
          }
          else{
            break;
          }
        } 
        else {
          arr.push_back(a[i]);
        }
      }
    }
    

  }

  cout << cnt;
  return 0;
}
