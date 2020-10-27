#include <iostream>
#include "stack.h"
void Stack::push(int x){
    Node *newnode=new Node(x);
    if(last==NULL){
        last=newnode;
    }
    else{
        newnode->next=last;
        last=newnode;
    }
}
int Stack::pop(){
    Node *temp=last;
    int ans=temp->data;
    last=temp->next;
    delete temp;
    return ans;
}