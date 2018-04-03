#include<stdio.h>

int main(){

    int t,i,j;
    scanf("%d",&t);

    for(i=0;i<t;i++){
        int win=0,ban1,ban2,pak1,pak2,i,j;

        for(j=0;j<2;j++){
            scanf("%d %d %d %d",&ban1,&ban2,&pak1,&pak2);
            if((ban1+ban2)>(pak1+pak2))
                win++;
        }
        if(win==2){
            printf("Banglawash\n");

        }else{
            printf("Miss\n");
        }

    }
return 0;
}
