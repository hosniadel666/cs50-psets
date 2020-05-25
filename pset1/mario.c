#include<stdio.h>
int main()
{
    int x;
    //enter the number of row
    //check if the numbers of rows is in range
    do
    {
        printf("Hight:");
        scanf("%d", &x);
    }
    while ((x < 1) || (x > 8));
    for (int i = 0 ; i < x ; i++)
    { 
        for (int j = i + 1 ; j < x ; j++)
        {
            printf(" ");
        }
        for (int k = i ; k >= 0; k--)
        {
            printf("#");
        }
        printf("\n");
    }
}
