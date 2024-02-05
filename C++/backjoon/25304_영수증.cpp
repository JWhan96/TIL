#include <iostream>

using namespace std;

int x, n, price, num, result;

void init() {
  price = num = 0;
}

void input() {
  cin >> price >> num;
} 

void sol(){
  result += price*num;
}

int main() {
  
  
  cin >> x >> n;
  for (int i=1; i <= n; i++){
    init();
    input();
    sol();
  }
  
  if (result == x){
    cout << "Yes";
  }
  else{
    cout << "No";
  }
  return 0;
}