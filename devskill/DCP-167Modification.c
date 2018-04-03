#include<stdio.h>

int main(){
    int input,c=1;
    scanf("%d",&input);
    while(input>0){
    int a,i=0,res;
    scanf("%d",&a);
    res = cube(a);
    printf("Case %d: %d",c,res);
    input--;
    c++;
    }
return 0;
}
int cube(int a){

return a*a*a;
}
