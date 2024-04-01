#include <stdio.h>
#include <stdlib.h>

int findDuplicate(int* nums, int numsSize)
{
  int* array;
  int i;
  int j;

  i = 0;
  j = 0;
  array = (int *)malloc((numsSize + 1) * sizeof(int));
  while (i < numsSize)
  {
    array[i] = -1;
    i++;
  }
  i = 0;
  while (i < numsSize)
  {
    if (array[nums[i]] != -1)
    {
      return (nums[i]);
    }
    else
    {
      array[nums[i]] = 0;
    }
    i++;
  }
  return(0);
}
