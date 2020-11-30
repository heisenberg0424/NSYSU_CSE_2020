#ifndef _WORD_H_
#define _WORD_H_
#include "Token.h"
#include "Tag.h"
class Word : public Token{
public:
    string lexeme="";
    Word(): Token(){}
    Word(string s,int tag):Token(tag){
        lexeme=s;
    }
    string toString(){
        return lexeme;
    }
    Word *and_c,*or_c,*eq,*ne,*ge,*le,*minus,*True,*False,*temp;
    
    bool operator!(){
        if (lexeme==""&& !tag)
            return false;
        return true;
    }
};

#endif
