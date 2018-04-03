#include<stdio.h>
int main(){

    int t,c,d,i=1;
    scanf("%d",&t);
    while(t>0){
        scanf("%d%d",&c,&d);
        printf("Case %d: %d\n",i,c+d);
        i++;
        t--;
    }
return 0;
}
