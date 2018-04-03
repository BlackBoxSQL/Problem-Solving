#include <stdio.h>
int main()
{
    int N=0,i,nm;
    scanf("%d",&N);
    for(i=1;i<=10;i++){

        nm=N*i;
        printf("%d x %d = %d\n",i,N,nm);
    }

    return 0;
}
