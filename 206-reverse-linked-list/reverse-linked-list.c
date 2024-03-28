/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * }jkhj;
 */
struct ListNode* reverseList(struct ListNode* head)
   {
    struct ListNode* root = head;
    int arr[9999999];
    int i;
   
    i = 0;
    while (head)
    {
    arr[i++] = head->val;
    head = head->next;
    }
    i--;
    head = root;
    while (head)
    {
   head->val = arr[i--];
   head = head->next;
   }
   return (root);
  }