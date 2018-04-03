#include<stdio.h>

int main(){
    
    int en,wh;
    double arph,SALARY;
    
    scanf("%d %d %lf",&en,&wh,&arph);
    
    SALARY=(arph*wh);
    
    printf("NUMBER = %d\n",en);
    printf("SALARY = U$ %0.2lf\n",SALARY);
return 0;
}