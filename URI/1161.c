#include<stdio.h>

int main(){

int M,N,fact,fact2,i,j;
while(scanf("%d %d",&M,&N)!=EOF){

    for(i = M; i>1;i--)

        fact = fact*i;

    for(j = N; j>1; j--)

        fact2 = fact2*j;

}
printf("%d",fact+fact2);

return 0;
}
