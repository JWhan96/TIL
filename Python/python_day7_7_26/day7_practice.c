//절차 지향 프로그래밍
// 함수를 연속으로 구성하는 프로그래밍 패러디

#include <stdio.h>

int add(int a, int b);

int main() {
    int num1 = 10;
    int num2 = 20;
    int result = add(num1, num2);
    printf('%d', result);
    return 0;
}
int add(int a, int b){
    return a+b;

}