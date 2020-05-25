#include<stdio.h>
#include<math.h>
#define a 25
#define b 10
#define c 5
#define d 1
int main()
{
    float dollar;
    int coin = 0, pins;
    do
    {
        printf("Change owed:");
        scanf("%f", &dollar);
    }
    while (dollar <= 0);
    //convert dollars into pins
    pins = round(dollar * 100);
    //check if pis is divisble by quarters
    if (pins % a == 0)
    {
        printf("%d\n", pins / a);
        return 0;
    }
    while (pins > a)
    { 
        coin++;
        pins -= a;	
    }
    while (pins >= b)
    { 
        coin++;
        pins -= b;	
    }
    while (pins >= c)
    { 
        coin++;
        pins -= c;
    }
    while (pins >= d)
    { 
        coin++;
        pins -= d;
    }
    //print the minimum numbe number of coins
    printf("%d\n", coin);	
}
