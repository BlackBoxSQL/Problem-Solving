times = int(input())
i = 0
while(times>i):
    nu = int(input())
    res = (nu*(nu+1))/2
    res*=res
    resf = (nu*(nu+1)*(2*nu+1))/6
    final = res-resf
    print(int(final))
    i=+1

#school math series dharar formula and square
#runtime errror
#c solve from net the long long is the prblm


#include<stdio.h>
#define ll long long
# int main()
#     {
#         int tc;
#         ll r,r1,n;
#         scanf("%d",&tc);
#         while(tc--){
#             n;
#             scanf("%lld",&n);
#             r=(n*(n+1))/2;
#             r*=r;
#             r1=(n*(n+1)*(2*n+1))/6;
#             printf("%lld\n",r-r1);
#         }
#         return 0;
#     }
