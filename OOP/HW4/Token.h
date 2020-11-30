#ifndef _TOKEN_H_
#define -TOKEN_H_
#include <sstream>
using namespace std;
class Token{
public:
    int tag=0;
    Token(){}
    Token(int t){tag=t;}
    virtual string toString(){
        string s;
        stringstream ss;
        ss<<tag;
        ss>>s;
        return s;
    }
};

#endif
