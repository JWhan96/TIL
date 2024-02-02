#include <iostream>

using namespace std;

int main() {
  int h, m, time;

  cin >> h >> m >> time;

  if ((m+time)>= 60){
    if (h+((m+time)/60)>=24){
      cout << (h+((m+time)/60))-24 << " " << (m+time)%60 << endl;
    }
    else{
      cout << h+((m+time)/60) << " " << (m+time)%60 << endl;
    }
  }
  else{
    cout << h << " " << m+time << endl;
  }

  return 0;
}