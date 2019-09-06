#include<iostream>
using namespace std;

int main(){
    int money, total_count = 0;
    cin >> money;
    int charge = 1024 - money;
    total_count += charge/64;
    total_count += (charge % 64)/16;
    total_count += (charge % 16)/4;
    total_count += (charge % 4);
    printf("%d",total_count);
    system("pause");

}