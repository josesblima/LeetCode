void reorderList(struct ListNode* head)
{
    struct ListNode* root = head;
    int i = 0;
    int j = 0;
    int z = 0;
    while (head)
    {
        i++;
        head = head->next;
    }
    head = root;
    int** array = malloc((i + 1) * sizeof(int*));
    while (j < i)
    {
        array[j] = head;
        j++;
        head = head->next;
    }
    array[j] = NULL;
    while (z < j)
    {
        z++;
    }
    z++;
    head = root;
    i = 1;
    z--;
    z--;
    while (i < z)
    {
        head->next = array[z];
        head = array[z];
        z--;
        if (i <= z)
        {
            head->next = array[i];
            head = head->next;
            i++;
        }
    }
    if (i <= z)
        {
            head->next = array[z];
            head = head->next;
        }
    head->next = NULL;
    while (root)
    {
        root = root->next;
    }
}
