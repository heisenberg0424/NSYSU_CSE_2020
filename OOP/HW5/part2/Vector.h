#include "Trace.h"
template <class T>
class Vector{
    static int cnt;
public:
    T *data;
    
    Vector(int size){
        TRACE(dummy,"vector<T>::vector(int)");
        cout<<" count = "<<++cnt<<endl;
        data=new T [size];
    }
    
    ~Vector(){
        TRACE(dummy,"vector<T>::~vector");
        cout<<" count = "<<cnt--<<endl;
    }
    
    T& operator[](int pos){
        return data[pos];
    }
};

template<> class Vector<void*>{
    static int cnt;
public:
    void **data;
    Vector(int size){
        TRACE(dummy,"vector<void*>::vector(int)");
        cout<<" count = "<<++cnt<<endl;
        data=new void*[size];
    }
    void*& elem(int i){return data[i];}
    ~Vector(){
        TRACE(dummy,"vector<void*>::~vector");
        cout<<" count = "<<cnt--<<endl;
    }
    //void*& operator[](int i){return data[i];}
};

template<class T> class Vector<T*>: public Vector<void*>{
public:
    typedef Vector<void*> Base;
    explicit Vector(int size):Base(size){
        TRACE(dummy,"vector<T*>::vector(int)");
    }
    T*& operator[] (int i){
        static T* t=(T*)Base::elem(i);
        return t;
    }
    ~Vector(){
        TRACE(dummy,"vector<T*>::~vector");
    }
    T*& elem(int i){
        static T* t=(T*)Base::elem(i);
        return t;
    }
};
template<class T>
int Vector<T>::cnt=0;
template<> int Vector<void *>::cnt;

