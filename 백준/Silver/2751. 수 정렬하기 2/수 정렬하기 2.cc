#include<cstdio>
main ()
{
  
int n, v, i, a[2000001] = { };
  
scanf ("%d", &n);
  
while (n--)
    scanf ("%d", &v), a[v+1000000] = 1;
  
for (i = 0; i < 2000001; ++i)
    if (a[i])
      printf ("%d\n", i-1000000);

}