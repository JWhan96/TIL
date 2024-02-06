#include <iostream>
#include <string>

using namespace std;

int main() {
    string word;
    cin >> word;

    int time = 0;
    for (char ch : word) {
        if (ch >= 'A' && ch <= 'C')
            time += 3;
        else if (ch >= 'D' && ch <= 'F')
            time += 4;
        else if (ch >= 'G' && ch <= 'I')
            time += 5;
        else if (ch >= 'J' && ch <= 'L')
            time += 6;
        else if (ch >= 'M' && ch <= 'O')
            time += 7;
        else if (ch >= 'P' && ch <= 'S')
            time += 8;
        else if (ch >= 'T' && ch <= 'V')
            time += 9;
        else if (ch >= 'W' && ch <= 'Z')
            time += 10;
    }

    cout << time << endl;
    
    return 0;
}

// #include <iostream>

// using namespace std;

// int total=0;
// string s;

// int main() {
//     cin >> s;

//     for(int i=0;i<s.size();i++) {
//         total+=((int)s[i]-65)/3 + 3; //아스키 코드로 계산

//         //예외 처리
//         if(s[i] == 'S' ||s[i] == 'V' ||s[i] == 'Y' ||s[i] == 'Z' ) total--;
//     }
//     cout << total;
// }
