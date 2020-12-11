#ifndef __TRACE_H_INCLUDED__
#define __TRACE_H_INCLUDED__

#include <iostream>
#include <string>
using namespace std;

class Trace{
public:
    Trace(const string n):name(n){
        depth++;
        print_name("Entering");
    }
    ~Trace(){
        print_name("Leaving ");
        depth--;
    }
private:
    static int depth;
    const string name;
    void print_name(const string prefix){
        for (int i=0;i<depth;i++)
            cerr<<" ";
        cerr<<prefix<<" "<<name<<" ("<<depth<<") "<<endl;
    }
};
#ifndef __TRACE__
#define TRACE(v,n)      Trace v(n)
#else
#define TRACE(v,n)
#endif

#endif
