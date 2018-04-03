#include<stdio.h>

int main(){

 int X,i=1;
 while(1){
    scanf("%d",&X);

    if(X!=0){

        for(i=1;i<=X;i++){
            printf("%d ",i);
        }
    }else
    {
        break;
    }
 }



}
