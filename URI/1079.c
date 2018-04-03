#include<stdio.h>

int main(){

    int a=0,in;
    float f,b,c,med,wf,wb,wc;

    scanf("%d",&in);

    for(a=0;a<in;a++){
        scanf("%f %f %f",&f,&b,&c);
        wf=f*2;
        wb=b*3;
        wc=c*5;
        med=(wf+wb+wc)/10;
        printf("%.1f\n",med);
    }
return 0;
}
