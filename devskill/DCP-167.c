#include<stdio.h>

int main()
{
    int t,n,i;
    scanf("%d",&t);
    for(i=1;i<=t;i++){
        int sum1,sum2;
        scanf("%d",&n);
        sum1=n*(n+1)/2;//equation /*both of these line can be writen in same formula*/
        sum2=sum1*sum1;//equation
        printf("Case %d: %d\n",i,sum2);
    }
    return 0;
}
