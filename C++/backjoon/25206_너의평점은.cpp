#include <iostream>
using namespace std;
int main() {
	string majorName; double avg = 0; float sumGrade = 0;
	double score[20]; float grade[20];
	string input;
	for (int i = 0; i < 20; ++i)
	{
		cin >> majorName >> grade[i] >> input;
		if (input == "A+") score[i] = 4.5;
		else if (input == "A0") score[i] = 4.0;
		else if (input == "B+") score[i] = 3.5;
		else if (input == "B0") score[i] = 3.0;
		else if (input == "C+") score[i] = 2.5;
		else if (input == "C0") score[i] = 2.0;
		else if (input == "D+") score[i] = 1.5;
		else if (input == "D0") score[i] = 1.0;
		else if (input == "F") score[i] = 0.0;
		else if (input == "P") { score[i] = 0.0; grade[i] = 0; }
		avg += (score[i] * grade[i]);
		sumGrade += grade[i];
	}
	avg = avg / sumGrade;
	cout << fixed;
	cout.precision(6);
	cout << avg;
}
// #include <iostream>
// #include <string>
// #include <algorithm>
// using namespace std;

// int main() {
//   int n = 20;
//   string subject, number, alpa;
//   double subscore;
//   double num1=0.0;
//   double score[20];
//   for (int i =0; i < 20; i++){
//     cin >> subject >> number >> alpa;
//     if (alpa == "A+"){
//       score[i] = stod(number)*4.5;
//       num1 += stod(number);
//     }
//     else if (alpa == "A0"){
//       score[i] = stod(number)*4.0;
//       num1 += stod(number);
//     }
//     else if (alpa == "B+"){
//       score[i] = stod(number)*3.5;
//       num1 += stod(number);
//     }
//     else if (alpa == "B0"){
//       score[i] = stod(number)*3.0;
//       num1 += stod(number);
//     }
//     else if (alpa == "C+"){
//       score[i] = stod(number)*2.5;
//       num1 += stod(number);
//     }
//     else if (alpa == "C0"){
//       score[i] = stod(number)*2.0;
//       num1 += stod(number);
//     }    
//     else if (alpa == "D+"){
//       score[i] = stod(number)*1.5;
//       num1 += stod(number);
//     }
//     else if (alpa == "D0"){
//       score[i] = stod(number)*1.0;
//       num1 += stod(number);
//     }
//     else if (alpa == "F"){
//       score[i] = stod(number)*0.0;
//       num1 += stod(number);
//     }
//     else if (alpa == "P"){
//       score[i] = 0;
//       // num1 += stod(number);
//     }
//   }
//   for (int i =0; i < 20; i++){
//     subscore += score[i];
//   }
//   cout << subscore/num1;

//   return 0;
// }
