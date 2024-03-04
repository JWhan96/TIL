// #include <iostream>
// #include <string>
// using namespace std;

// int main(){
//   string str;
//   int cnt=0;
//   char i='3';
//   cin >> str;
//   for(int index=0; index < str.length(); index++){
//     if(str[index]==i){
//       cnt++;
//     }
//   }
//   cout << cnt;

//   return 0;
// }
#include <iostream>
#include <string>
using namespace std;

int main(){
  string str;
  int arr[10]= {0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0};
  cin >> str;
  for(int index=0; index < str.length(); index++){
    arr[str[index]-'0']++;
  }
  for(int i=0; i<10; i++){
    cout << arr[i] << endl;
  }

  return 0;
}