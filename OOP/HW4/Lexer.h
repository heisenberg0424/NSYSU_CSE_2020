#ifndef _LEXER_H_
#define _LEXER_H_
#include <map>
#include <cstdlib>
#include "Type.h"
#include "Num.h"
#include "Real.h"

class Lexer{
public:
    int line=1;
    char peek=' ';
    void reserve(Word w);
    int peek_tmp=0;
    Word word;
    Type type;
    map<string,Word> words;
    void reserve(Word w){
        words[w.lexeme]=w;
    }
    Lexer(){
        Word *tmp = new Word("if", Tag::IF);
        reserve(*tmp);
        tmp = new Word("else", Tag::ELSE);
        reserve(*tmp);
        tmp = new Word("while", Tag::WHILE);
        reserve(*tmp);
        tmp = new Word("do", Tag::DO);
        reserve(*tmp);
        tmp = new Word("break", Tag::BREAK);
        reserve(*tmp);
        delete tmp
        word.and_c = new Word("&&", Tag::AND);
        word.or_c = new Word("||", Tag::OR);
        word.eq = new Word("==", Tag::EQ);
        word.ne = new Word("!=", Tag::NE);
        word.le = new Word("<=", Tag::LE);
        word.ge = new Word(">=", Tag::GE);
        word.minus = new Word("minus", Tag::MINUS);
        word.True = new Word("true", Tag::TRUE);
        word.False = new Word("false", Tag::FALSE);
        word.temp = new Word("t", Tag::TEMP);
        reserve(*word.True);
        reserve(*word.False);
        type.Int = new Word("int", Tag::BASIC);
        type.Float = new Type("float", Tag::BASIC, 8);
        type.Char = new Type("char", Tag::BASIC, 1);
        type.Bool = new Type("bool", Tag::BASIC, 1);

        reserve(*type.Int);
        reserve(*type.Char);
        reserve(*type.Bool);
        reserve(*type.Float);
    }
    
    void readch(int flag=0){
        int i=getchar();
        if(flag){
            peek_tmp=i;
            if (i != ' ' && i != '\n' && i != -1 && (isalpha((char)i) || isdigit((char)i)))
                cout << (char)i;
        }
        else{
            if (i != ' ' && i != '\n' && i != -1)
                cout << (char)i;
        }
        
        if (i != -1)
            peek = (char)i;
        else{
            cout << "End of file reached" << endl;
            exit(1);
        }
    }
    
    bool readch(char c){
        readch();
        if (peek != c)
            return false;
        peek = ' ';
        return true;
    }
    Token scan(int count){
        if(cin.peek() != -1)
            cout<<count<<".\tToken: ";
        if(peek_tmp && peek_tmp != ' '){
            cout<< (char)peek_tmp;
            peek_tmp=0;
        }
        
        for (;;readch()){
            if(peek== ' '|| peek =='\t')
                continue;
            else if (peek=='\n')
                line++;
            else
                break;
        }
        switch(peek){
            case '&':
                if (readch('&'))
                    return *word.and_;
        }
    }
    
}
#endif
