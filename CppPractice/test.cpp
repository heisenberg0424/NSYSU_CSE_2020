#include <iostream>
using std::cout;
using std::endl;
int main(){
    int a[5][4][3];
    cout<<&a[0][0]-&a[1][2]<<endl;
}