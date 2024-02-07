```c++
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
```
- push_back(), pop_back(), insert(), erase(), sort(), find()

```c++
#include <iostream>
#include <map>
#include <string>

using namespace std;

int main() {
    map<string, int> dictionary;
    dictionary["apple"] = 10;
    dictionary["banana"] = 20;

    // 딕셔너리의 모든 키-값 쌍 출력
    for (const auto& kv : dictionary) {
        cout << "Key: " << kv.first << ", Value: " << kv.second << endl;
    }

    // 특정 키에 해당하는 값 찾기
    string key = "banana";
    if (dictionary.find(key) != dictionary.end()) {
        cout << "Value of key '" << key << "': " << dictionary[key] << endl;
    } else {
        cout << "Key '" << key << "' not found." << endl;
    }

    return 0;
}
```