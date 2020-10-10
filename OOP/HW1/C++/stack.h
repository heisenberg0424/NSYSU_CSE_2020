#ifndef __STACK_H__
#define __STACK_H__
class Node{
public:
    int data;
    Node *next;
    Node(int x){
        data=x;
    }
};
class Stack{
public:
    Node *last;
    Stack(){
        last=NULL;
    }
    void push(int x);
    int pop();


};



#endif