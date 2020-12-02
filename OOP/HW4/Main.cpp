#include "Lexer.h"
using namespace std;
int main(){
    Lexer lexer;
    int count=1;
    while(1){
        Token t=lexer.scan(count++);
        int token = atoi(t.toString().c_str());
        if(token>255)
            type(token);
        else
            cout<<"\t("<<(char)token<<")"<<endl;
        
    }
}