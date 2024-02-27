#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main(){
  char word[101];
  cin >> word;
  int arr[26];
  int index = 0;
  int index2 = 0;

  for(int i=0; i<26; i++){
    arr[i] = -1;
  }

  while(word[index]!='\0'){
    index2 = (word[index] - 'a');
    if(arr[index2] == -1){
      arr[index2] = index;
    }
    index++;
  }

  for(int i=0; i<26; i++){
    cout << arr[i] << " ";
  }

  return 0;
}