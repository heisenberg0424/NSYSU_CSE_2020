#include "Complex.h"
#include <cmath>
using namespace std;
double pi=M_PI;

double Complex::Real(){return real;}
double Complex::Imag(){return imag;}

double Complex::Norm(){return real*real+imag*imag;}
double Norm(const Complex &x){return x.real*x.real+x.imag*x.imag;}

double Complex::Abs(){return sqrt(Norm());}
double Abs(const Complex &x){return sqrt(Norm(x));}

double Complex::Arg(){
    if(imag!=0){
        return 2*atan(imag/(Abs()+real));
    }
    else if (imag>0)
        return 0;
    else 
        return pi;
}
double Arg(const Complex &x){
    Complex temp(x);
    return temp.Arg();
}

ostream& operator<<(ostream &o,const Complex &x){
    o<<'('<<x.real<<','<<x.imag<<')';
    return o;
}

Complex::Complex(const double re,const double im){
    real=re;
    imag=im;
}

Complex::Complex(const Complex &c){
    real=c.real;
    imag=c.imag;
}

Complex& Complex::operator=(const Complex &c){
    this->real=c.real;
    this->imag=c.imag;
    return *this;
}

Complex Complex::operator++(){
    real++;
    imag++;
    return *this;
}
Complex Complex::operator++(int){
    Complex temp=*this;
    real++;
    imag++;
    return temp;
}
Complex Complex::operator--(){
    real--;
    imag--;
    return *this;
}
Complex Complex::operator--(int){
    Complex temp=*this;
    real--;
    imag--;
    return temp;
}

Complex Complex::Polar(const double leng,const double arg){
    this->real=leng*cos(arg);
    this->imag=leng*sin(arg);
    return *this;
}
Complex Polar(const double leng,const double arg){
    Complex *temp=new Complex();
    temp->imag=leng*sin(arg);
    temp->real=leng*cos(arg);
    return *temp;
}

Complex operator+(const Complex &x,const Complex &y){
    Complex *temp=new Complex(x.real+y.real,y.imag+x.imag);
    return *temp;
}
Complex operator-(const Complex &x,const Complex &y){
    Complex *temp=new Complex(x.real-y.real,x.imag-y.imag);
    return *temp;
}
Complex operator*(const Complex &x,const Complex &y){
    Complex *temp=new Complex();
    temp->real=(x.real)*(y.real)-(x.imag)*(y.imag);
    temp->imag=(x.real)*(y.imag)+(y.real)*(x.imag);
    return *temp;
}
Complex operator/(const Complex &x,const Complex &y){
    double a=x.real,b=x.imag,c=y.real,d=y.imag;
    Complex *temp=new Complex();
    temp->real=(a*c+b*d)/(c*c+d*d);
    temp->imag=(b*c-a*d)/(c*c+d*d);
    return *temp;
}

Complex operator+=(Complex &x,const Complex &y){
    x.imag+=y.imag;
    x.real+=y.real;
    return x;
} 
Complex operator-=(Complex &x,const Complex &y){
    x.imag-=y.imag;
    x.real-=y.real;
    return x;
}
Complex operator*=(Complex &x,const Complex &y){
    x=x*y;
    return x;
} 
Complex operator/=(Complex &x,const Complex &y){
    x=x/y;
    return x;
} 

bool operator==(const Complex &x,const Complex &y){
    if(x.real==y.real&&x.imag==y.imag)
        return 1;
    return 0;
}
bool operator!=(const Complex &x,const Complex &y){
    return !(x==y);
}
Complex::~Complex(){}


