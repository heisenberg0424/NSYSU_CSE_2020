#include "Token.h"
class Word : public Token{
public:
    string lexeme="";
    Word(string s,int t){
        tag=t;
        lexeme=s;
    }
    string toString(){
        return lexeme;
    }
    Word
    and_c    =new Word("&&",   Tag.AND),
    or_c     =new Word("||",   Tag.OR),
    eq       =new Word("==",   Tag.EQ),
    ne       =new Word("!=",   Tag.NE),
    ge       =new Word(">=",   Tag.GE),
    le       =new Word("<=",   Tag.LE),
    minus    =new Word("minus",Tag.MINUS),
    True     =new Word("true" ,Tag.TRUE_c),
    False    =new Word("false",Tag.FALSE_c),
    temp     =new Word("t",    Tag.TEMP);
}
