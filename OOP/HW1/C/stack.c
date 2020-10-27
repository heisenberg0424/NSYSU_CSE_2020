#include <stdlib.h>
#include "stack.h"

void push(struct stack* this, int x){
    struct node *new = malloc(sizeof(struct node));
    new->data=x;
    if (this->tail==NULL){
        this->tail=new;
    }
    else{
        struct node *stk = this->tail;
        new->next=this->tail;
        this->tail=new;
    }
}

int pop(struct stack* this){
    int temp=this->tail->data;
    struct node *del=this->tail;
    this->tail=this->tail->next;
    free(del);
    return temp;
}

struct stack* new_stack(){
    struct stack* stk = malloc(sizeof(struct stack));
    return stk;
}

void delete_stack(struct stack* stk){
    struct node *temp=stk->tail;
    struct node *iter=temp;
    while( temp!=NULL ){
        iter=temp;
        temp=iter->next;
        free(iter);
    }
    free(stk);
}
