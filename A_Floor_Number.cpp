#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int main()
{int a;
cin>>a;
while(a--){
int x,y;
 scanf("%d %d", &x,&y);
 if(x==1||x==2){
     printf("%d\n", 1);
     continue;
 }
 else
 {
     int z=(x-3)/y;
     printf("%d\n", z+2); 
 }
 
}
return 0;
}