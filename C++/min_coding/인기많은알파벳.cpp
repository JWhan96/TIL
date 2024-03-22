#include <iostream>
#include <string>

using namespace std;

int main(){
  string str;
  cin >> str;
  int arr[256] = {0, };
  int max_a = 0;
  string result;
  for(int i = 0; str[i]; i++ ){
    arr[ str[i] ]++;
    if (arr[str[i]] >= max_a){
      result = result + 'A';
      cout << result;
      max_a = arr[str[i]];
      result = str[i];
    }
  }
  cout << result;

  return 0;
}

// #include <iostream>

// using namespace std;

// int main()
// {
// 	char arr[9];
// 	int DAT[27] = { 0, };

// 	cin >> arr;

// 	for (int i = 0; i < 8; i++) {
// 		DAT[arr[i] - 'A']++;
// 	}

// 	int max_cnt = 0;
// 	char c;
// 	for (int i = 0; i < 27; i++) {
// 		if (max_cnt < DAT[i]) {
// 			max_cnt = DAT[i];
// 			c = i + 'A';
// 		}
// 	}

// 	cout << c;

// 	return 0;
// }