#include "Word.h"
class Type : public Word{
public:
    int width=0;
    Type(string s,int t,int w){
        tag=t;
        lexeme=s;
        width=w;
    }
};
