
int lengthOfLastWord(char* s) {
  int i;
  int res;

  i = 0;
  res = 0;
  while (s[i])
  {
    i++;
  }
  i--;
  while (i >= 0 && s[i] == ' ')
    i--;
  while (i >= 0)
  {
    if (s[i] == ' ')
    {
      return (res);
    }
    res++;
    i--;
  }
  return (res);
}

