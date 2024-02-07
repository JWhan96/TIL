#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

int main() {
  string a, b;
  cin >> a;
  b = a;
  reverse(a.begin(), a.end());
  if (a==b){
    cout << 1;
  }
  else{
    cout << 0;
  }
  return 0;
}