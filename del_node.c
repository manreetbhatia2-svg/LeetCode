// Q237 of leetcode. Delete a node given without accessing head
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
    
void deleteNode(struct ListNode* node) {
    node->val = node->next->val;
    node->next = node->next->next;

}
 