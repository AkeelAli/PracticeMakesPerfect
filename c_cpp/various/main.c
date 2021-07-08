#include <stdio.h>
#include <stdlib.h>

typedef struct node_ {
    int val;
    struct node_* next;
} node_t;


void printlist(node_t *node) {

    while(node) {
        printf("%d", node->val);
        if (node->next) printf("->");
        else printf("\n");
        node = node->next;
    }    

    return;
}

int main(void) {

    node_t *node = NULL, *prev_node = NULL, *head = NULL;
    int i = 0;


    for (i = 0; i < 10; i++) {
        node = malloc(sizeof(node_t));
        if (!node) return -1;

        node->val = i;
        if (prev_node) {
            prev_node->next = node;
        } else {
            head = node;
        }
        prev_node = node;
    }
    if (prev_node) {
        prev_node->next = NULL;
    }
    
    node = head;

    printlist(head);
    
    node_t arr[10];

    arr[0].val = 10;
    arr[0].next = &arr[1];

    arr[1].val = 20;
    arr[1].next = NULL; 

    printlist(&arr[0]);

    return 0;
}
