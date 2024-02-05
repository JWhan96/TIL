#include <iostream>
#include <cstdio>
using namespace std;


  int tc, T, a, b, result;
void init(){
  a = b = 0;
}

void input() {
  cin >> a >> b;
}

void sol(){
  result = a + b;
}

int main() {
  ios::sync_with_stdio(0);
  cin.tie(0);
  
  cin >> T;
  for (tc=1; tc <= T; tc++){
    init();
    input();
    sol();
    printf("Case #%d: %d\n", tc, result);
  }
  return 0;
}