#ifndef _NUM_H_
#define _NUM_H_
#include "Tag.h"
#include "Token.h"
class Num;public Token{
public:
    int value;
    Num(int v):Token(Tag::NUM){
        value=v;
    }
    virtual string toString(){
        string s;
        string ss;
        ss<<value;
        ss>>s;
        return s;
    }
};

#endif
