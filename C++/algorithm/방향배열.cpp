#include <iostream>

using namespace std;

int main(){
  int arr[5][5] = {0, };

  int row=2, col=3;

  // 다음과 같은 형식을 쓰게 된다면 예외처리도 일일이 해주어야하고
  // 실수할 가능성이 늘어난다.
  // 그러므로 방향배열을 미리 지정해 놓는 것이 좋다.
  // arr[row][col] = 1;
  // arr[row -1][col -1] = 1; // 좌측상단
  // arr[row -1][col +1] = 1; // 우측상단
  // arr[row +1][col +1] = 1; // 우측하단
  // arr[row +1][col -1] = 1; // 좌측하단

  // 미리 방향배열 지정
  int dr[] = { -1, -1, 1, 1 };
  int dc[] = { -1, 1, 1, -1 };

  for (int i = 0; i < 4; i++){
    for (int d = 1; d < 5; d++){ // d거리만큼 퍼지는 경우
      int nr = row + dr[i] * d;
      int nc = col + dc[i] * d;
      
      if (nr < 0 || nc < 0 || nr >= 5 || nc >= 5){
        // 맵바깥으로 넘어가는 경우 예외처리
        continue;
      }
      arr[nr][nc] = 3;
    }
  }

  for (int i = 0; i < 5; i++){
    for (int j=0; j < 5; j++){
      cout << arr[i][j];
    }
    cout << endl;
  }
  return 0;
}