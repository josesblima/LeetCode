
struct ListNode* removeNthFromEnd(struct ListNode* head, int n)
{
    int i;
    struct  ListNode* root;
    int j;

    i = 0;
    j = 0;
    root = head;
    while (root)
    {
      root = root->next;
      i++;
    }
    if (i == n)
    {
      head = head->next;
      return (head);
    }
    root = head;
    while (j < i - n - 1)
    {
      root = root->next;
      j++;
    }
    if (n > 1)
      root->next = root->next->next;
    else
      root->next = NULL;
    return (head);

}