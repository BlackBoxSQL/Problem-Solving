#include<stdio.h>

int main(){

    int a,b,i=0,t=1,tt,fnum=0,snum=0,j=0,res=0;
    scanf("%d",&tt);

    for(t=1;t<=tt;t++){
        scanf("%d %d",&a,&b);

        for(i=0;i<=a;i++){

            if(i%3==0){
                fnum++;
            }

        }
         for(j=0;j<=b;j++){

                if(j%3==0){
                    snum++;

                }
            }
        res=fnum+snum;
        printf("Case %d: %d\n",t,res);
    }


}
