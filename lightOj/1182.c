#include<stdio.h>

int main(){

    int t,a,i=1,countone;
    scanf("%d",&t);

    while(t>0){
        scanf("%d",&a);

            if(a%2==1){
                countone++;
            }


            if(a%2==0){
                printf("Case %d: even\n",i);
            }
            else{
                printf("Case %d: odd\n",i);
            }

        i++;
        t--;
    }


}
