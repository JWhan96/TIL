#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std; 
int main() {
    // 5줄을 입력 받음
    string input;
    vector<string> lines;

    int max_length = 0;
    for (int i = 0; i < 5; ++i) {
        getline(cin, input);
        lines.push_back(input);
        max_length = max(max_length, static_cast<int>(input.length()));
    }

    // 벡터를 초기화하고 문자열을 채움
    vector<vector<char>> arr(max_length, vector<char>(5, ' '));
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < lines[i].length(); ++j) {
            arr[j][i] = lines[i][j];
        }
    }

    // 행과 열을 바꿔서 출력
    for (int i = 0; i < max_length; ++i) {
        for (int j = 0; j < 5; ++j) {
            if (arr[i][j] != ' ') {
                cout << arr[i][j];
            }
        }
        
    }

    return 0;
}
