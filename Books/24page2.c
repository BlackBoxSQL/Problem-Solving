#include<stdio.h>
#include<math.h>

int main(){
    float a,b,c,ab,s;

    scanf("%f %f %f",&a,&b,&c);

    s=(a+b+c)/2;

    ab = sqrt(s*(s-a)*(s-b)*(s-c));

    printf("%.5f",ab);


return 0;
}
