#ifndef __STACK_H__
#define __STACK_H__


struct node{
    int data;
    struct node *next;
};

struct stack{
    struct node *tail;
};

extern void push(struct stack* this, int x);
extern int pop(struct stack* this);
extern struct stack* new_stack();
extern void delete_stack(struct stack* stk);

#endif
