#include<stdio.h>
/*
cdp = code of product
ppu = price per unit
atp = amount to be paid
*/
int main(){

      int cdp1,nu1,cdp2,nu2;
      double ppu1,ppu2,atp1,atp2,fatp;
      scanf("%d %d %lf",&cdp1,&nu1,&ppu1);
      scanf("%d %d %lf",&cdp2,&nu2,&ppu2);
      atp1=(nu1*ppu1);
      atp2=(nu2*ppu2);
      fatp=atp1+atp2;
      printf("VALOR A PAGAR: R$ %0.2lf\n",fatp);


return 0;
}
