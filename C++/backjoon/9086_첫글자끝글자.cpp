#include <iostream>
#include <string>

using namespace std;

int main() {
  int n, b;
  cin >> n;
  cin.ignore();
  string a;
  while (getline(cin, a)){
    b = a.length();
    cout << a[0] << a[b-1] << endl;
  }
  return 0;
}