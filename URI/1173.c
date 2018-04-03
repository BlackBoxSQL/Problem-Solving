#include<stdio.h>

int main(){

  int n[10],i=0,a;
    scanf("%d",&a);

        for(i=0;i<10;i++){
            printf("N[%d] = %d\n",i,a);
             a=a+a;
        }
}
