#ifndef _REAL_H_
#define _REAL_H_
#include "Token.h"
#include "Tag.h"

class Real : public Token{
public :
    float value;
    Real(float v):Token(Tag::REAL){
        value=v;
    }
    virtual string toString(){
        string s;
        stringstream ss;
        ss<<value;
        ss>>s;
        return s;
    }
};

#endif
