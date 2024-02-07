#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
  string a, b;
  a = "abcde";
  b = a;
  reverse(a.begin(), a.end());  

  cout << a << " "<< b;

  return 0;
}