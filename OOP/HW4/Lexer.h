#ifndef _LEXER_H_
#define _LEXER_H_
#include <map>
#include <cstdlib>
#include <iostream>
#include "Type.h"
#include "Num.h"
#include "Real.h"
using namespace std;

class Lexer{
public:
    int line=1;
    char peek=' ';
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
        delete tmp;
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
                    return *word.and_c;
                else
                    return Token('&');
            case '|':
                if (readch('|'))
                    return *word.or_c;
                else 
                    return Token('|');
            case '=':
                if (readch('='))
                    return *word.eq;
                else
                    return Token('=');
            case '!':
                if (readch('='))
                    return *word.ne;
                else 
                    return Token('!');
            case '<':
                if (readch('='))
                    return *word.le;
                else
                    return Token('<');
            case '>':
                if (readch('='))
                    return *word.ge;
                else
                    return Token('>');
        }
        
        if (isdigit(peek)){
            int v=0;
            do{
                v=10*v+atoi(&peek);
                readch(1);
            }while(isdigit(peek));
            if(peek!='.')
                return Num(v);
            peek_tmp=0;
            cout<<peek;
            float x=v;
            float d=10;
            while(1){
                readch();
                if(!isdigit(peek))
                    break;
                x=x+atoi(&peek)/d;
                d*=10;
            }
            return Real(x);
        }
        if (isalpha(peek)){
            string b="";
            do{
                b+=peek;
                readch(1);
            }while(isalpha(peek) || isdigit(peek));
            string s=b;
            Word w=words[s];
            if(!w)
                return w;
            w=Word(s,Tag::ID);
            words[s]=w;
            return w;
        }

        Token tok(peek);
        peek=' ';
        return tok;
    }  
};

void type(int token){
    switch (token){
        case Tag::AND:
            cout<<"\t(AND)"<<endl;
            break;
        case Tag::BASIC:
            cout<<"\t(BASIC)"<<endl;
            break;
        case Tag::BREAK:
            cout<<"\t(BREAK)"<<endl;
            break;
        case Tag::DO:
            cout<<"\t(DO)"<<endl;
            break;
        case Tag::ELSE:
            cout<<"\t(ELSE)"<<endl;
            break;
        case Tag::EQ:
            cout<<"\t(EQ)"<<endl;
            break;
        case Tag::FALSE:
            cout<<"\t(FALSE)"<<endl;
            break;
        case Tag::GE:
            cout<<"\t(GE)"<<endl;
            break;
        case Tag::ID:
            cout<<"\t(ID)"<<endl;
            break;
        case Tag::IF:
            cout<<"\t(IF)"<<endl;
            break;
        case Tag::INDEX:
            cout<<"\t(INDEX)"<<endl;
            break;
        case Tag::LE:
            cout<<"\t(LE)"<<endl;
            break;
        case Tag::MINUS:
            cout<<"\t(MINUS)"<<endl;
            break;
        case Tag::NE:
            cout<<"\t(NE)"<<endl;
            break;
        case Tag::NUM:
            cout<<"\t(NUM)"<<endl;
            break;
        case Tag::OR:
            cout<<"\t(OR)"<<endl;
            break;
        case Tag::REAL:
            cout<<"\t(REAL)"<<endl;
            break;
        case Tag::TEMP:
            cout<<"\t(TEMP)"<<endl;
            break;
        case Tag::TRUE:
            cout<<"\t(TRUE)"<<endl;
            break;
        case Tag::WHILE:
            cout<<"\t(WHILE)"<<endl;
            break;
    }
}

#endif
