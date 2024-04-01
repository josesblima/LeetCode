#include <stdio.h>
#include <stdlib.h>

struct Node* copyRandomList(struct Node* head) {
  struct Node* root;
  struct Node* dcopy;
  struct Node* dcopyroot;
  struct Node* dclilhead;
  int len;
  int *array;
  struct Node* lilhead;
  int i;
  int   j;

  root = head;
  dcopy = malloc(sizeof(struct Node));
  dcopyroot = dcopy;
  len = 0;
  j = 0;
  if (head == NULL)
    return (NULL);
  while (head) // Get length of ll
  {
    len++;
    head = head->next;
  }
  head = root;
  array = (int *)malloc(len * sizeof(int));
  i = 0;
  while (i < len) // Fill array with -1
  {
    array[i] = -1;
    i++;
  }
  i = 0;
  while (head) // Fill in the array with the position where the random leads to
  {
    lilhead = root;
    i = 0;
    if (head->random != NULL)
    {
        while (lilhead)
        {
            if (lilhead == head->random)
            {
                array[j] = i;
                break;
            }
            lilhead = lilhead->next;
            i++;
        }
    }
    head = head->next;
    j++;
  }
  head = root;
  i = 0;
  while (head) // Malloc the deepcopy, link them and atribute their values
  {
    dcopy->val = head->val;
    head = head->next;
    if (i == len - 1)
    {
        dcopy->next = NULL;
        break;
    }
    dcopy->next = malloc(sizeof(struct Node));
    dcopy = dcopy->next;
    i++;
  }
  head = root;
  i = 0;
  j = 0;
  dcopy = dcopyroot;
  while (dcopy) // Doing the random
  {
    dclilhead = dcopyroot;
    j = 0;
    if (array[i] != -1)
    {
      while (j < array[i])
      {
        dclilhead = dclilhead->next;
        j++;
      }
      dcopy->random = dclilhead;
    }
    else
    {
      dcopy->random = NULL;
    }
    dcopy = dcopy->next;
    i++;
  }
  return (dcopyroot);
}