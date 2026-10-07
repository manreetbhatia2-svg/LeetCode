#include<stdio.h>
#include<stdlib.h>

struct queue{
    int time;
    struct queue*next;
}*head, *curr, *del, *p;

struct queue* RecentCounter();
int ping (int t,struct queue** head);

int main(){
    int num_of_msg;
    head = RecentCounter();

    num_of_msg = ping(1,&head);
    printf("no. of pings = %d\n",num_of_msg);
    num_of_msg = ping(50,&head);
    printf("no. of pings = %d\n",num_of_msg);
    num_of_msg = ping(300,&head);
    printf("no. of pings = %d\n",num_of_msg); 
    num_of_msg = ping(3001,&head);
    printf("no. of pings = %d\n",num_of_msg); 


}

struct queue* RecentCounter(){
    head = (struct queue*)malloc(sizeof(struct queue));
    head->time = 0;
    head->next=NULL;

    return head;
}

int ping (int t, struct queue** head){ 
    curr = *head;
    int count=0;

    // creating new node
    p = (struct queue*)malloc(sizeof(struct queue));
    p->time = t;
    p->next = NULL;

    // if its the first node
    if((*head)->time==0){
        del = *head;
        *head = p;
        curr = *head;
        free(del);
    }
    else{
        // adding further new node
        while(curr->next!= NULL){
            curr = curr->next;
        }
        curr->next = p;
    }
    curr = *head;
    // removing calls more than 3000ms
    while(curr != NULL && t - curr->time>3000 ){
        del = curr;
        curr=curr->next;
        free(del);
    }
    *head = curr;

    // counting number of nodes
    curr = *head;
    while(curr!=NULL){
        curr = curr->next;
        count++;
        
    }
    return (count);

}