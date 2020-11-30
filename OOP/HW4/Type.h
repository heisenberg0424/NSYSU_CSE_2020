#ifndef _TYPE_H_
#define _TYPE_H_
#include "Word.h"
class Type : public Word{
public:
    int width=0;
    Type():Word(){}
    Type(string s,int tag,int w):Word(s,tag){
        width=w;
    }
    Word *Int,*Float,*Char,*Bool;
    
    bool numeric(Word p){
        if ((p.tag == Type::Char->tag && p.lexeme == Type::Char->lexeme) || (p.tag == Type::Int->tag && p.lexeme == Type::Int->lexeme) || (p.tag == Type::Float->tag && p.lexeme == Type::Float->lexeme))
            return true;
        else
            return false;
    }
};

#endif
