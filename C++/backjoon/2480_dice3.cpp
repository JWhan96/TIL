#include <iostream>

using namespace std;

int main() {
  int a, b, c, max1, max2, result;

  cin >> a >> b >> c;

  if ( a == b && b == c ){
    result = 10000 + a*1000;
  }
  else if ((a == b) && (a != c)){
    result = 1000 + a*100;
  }
  else if ((a == c) && (b != c)){
    result = 1000 + a*100;
  } 
  else if ((c == b) && (a != c)){
    result = 1000 + b*100;
  }
  else {
    max1 = max(a, b);
    max2 = max(c, max1);
    result = 100 * max2;
  }
  
  cout << result << endl;

  return 0;
}