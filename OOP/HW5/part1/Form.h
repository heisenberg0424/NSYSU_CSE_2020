
#include <iostream>
#include <iomanip>
using namespace std;

void restore(){
    cout.precision(6);
    cout.unsetf ( std::ios::floatfield );
}

class Form{
private:
    int pre;
    bool fix_flag;
    bool sci_flag;
    double value;
public:
    Form(int pre):pre(pre),fix_flag(0),sci_flag(0){}
    void operator=(const Form &a){
        pre=a.pre;
    }
    Form operator()(double val){
        value=val;
        return *this;
    }
    Form &scientific(){
        sci_flag=1;
        return *this;
    }
    Form &fixed(){
        fix_flag=1;
        return *this;
    }
    Form precision(int x){
        pre=x;
        return *this;
    }
    
    friend ostream& operator<<(ostream& os, const Form &a);
    
};
ostream& operator<<(ostream& os, const Form &a){
    //streamsize ss = cout.precision();
    os.precision(a.pre);
    if (a.sci_flag){
        os<<scientific<<a.value;
        restore();
        return os;
    }
    if (a.fix_flag){
        os<<fixed<<a.value;
        restore();
        return os;
    }
    os<<a.value;
    restore();
    return os;
}
