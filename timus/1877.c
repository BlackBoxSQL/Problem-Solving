#include<stdio.h>
int main(void){
int a, b;
scanf("%d %d", &a, &b);

 if(a%2==0 || b%2!=0)
    printf("yes");
 else
    printf("no");
return 0;
}
