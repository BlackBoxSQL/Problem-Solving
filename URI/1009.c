#include<stdio.h>
int main(){

    char sn[50];
    double fs,bns,ts,add;
    scanf("%s",&sn);
    scanf("%lf %lf",&fs,&bns);

    add=(bns*15)/100;
    ts=fs+add;
    printf("TOTAL = R$ %0.2lf\n",ts);
//15% bonus with main

return 0;
}
