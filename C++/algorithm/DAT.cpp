#include <iostream>
#include <string>
using namespace std;
// // 어떤 특정한 문자의 개수 세는 법
// int main(){
//   string str = "1427445293";
//   int cnt=0;
//   char i='4';

//   for(int index=0; index < str.length(); index++){
//     if(str[index]==i){
//       cnt++;
//     }
//   }
//   cout << cnt;

//   return 0;
// }

// // 내가 가진 어떤 숫자의 개수 전부 세는 법
// int main(){
//   string str = "1427445293";
//   int arr[10]= {0, 0, 0, 0 ,0 ,0 ,0 ,0 ,0 ,0};

//   for(int index=0; index < str.length(); index++){
//     arr[str[index]-'0']++;
//   }
//   for(int i=0; i<10; i++){
//     cout << arr[i] << endl;
//   }

//   return 0;
// }

// // 숫자뿐 아니라 문자도 가능
// int main(){
//   char str[100] = "ACVIDKJCFCEICCCXXAFEWAAFWOOD";

//   int DAT[256] = {0, }; // 모든 요소 초기화를 다음과 같이 하는경우는 0만 가능

//   for (int i = 1; str[i]; i++){
//     DAT[str[i]]++;
//   }

//   cout << DAT['A'] << endl;
//   cout << DAT['C'] << endl;
//   cout << DAT['X'] << endl;

//   return 0;
// }

// 두개의 이어져 있는 문자를 확인 하는 법
// 2차원으로 만들어주면 된다
int main(){
  char str[100] = "ACVIDKJCFCEICCCXXAFEWAAFWOOD";

  int DAT[256][256] = {0, }; // 모든 요소 초기화를 다음과 같이 하는경우는 0만 가능
  
  for (int i = 1; str[i]; i++){
    DAT[str[i-1]][str[i]]++;
  }

  cout << DAT['A']['C'] << endl;
  cout << DAT['C']['A'] << endl;
  cout << DAT['C']['C'] << endl;
  cout << DAT['X']['A'] << endl;

  return 0;
}