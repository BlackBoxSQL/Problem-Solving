#include<stdio.h>
int main(){

    int value,i=1;
    scanf("%d",&value);

    for(i=1;i<=value;i++){

        if(value%i==0){
            printf("%d\n",i);
        }

    }


return 0;
}

