#include<cs50.h>
#include <stdio.h>
#include<string.h>
#include<ctype.h>
#include<math.h>
#include<stdlib.h>
char cipher_upper(char a, int b); // to encrypt a opper case letter
char cipher_lower(char a, int b); // to encrypt a opper case letter
int main(int argc, string argv[])
{
    int key;
    string check;
    if ((argc == 1) || (argc > 2))
    {
        printf("./caesar key\n");
        return 1;

    }

    for (int i = 0 ; i < strlen(argv[1]); i++)
    {
        check = argv[1];
        if (!isdigit(check[i]))
        {
            printf("./caesar key\n");
            return 1;
        }
    }

    key = atoi(argv[1]);
    printf("success\n%d\n", key);
    string str = get_string("enter plain text:");

    for (int i = 0; i < strlen(str); i++)
    {
        if (isalpha(str[i]))
        {
            if (isupper(str[i]))
            {
                str[i] = cipher_upper(str[i], key);
            }
            else if (islower(str[i]))
            {
                str[i] = cipher_lower(str[i], key);
            }
        }
        else
        {
            str[i] = str[i];
        }
    }
    printf("ciphertext:%s\n", str);
}


char cipher_upper(char a, int b)
{
    int x = a + b;
    if (x > 'Z')
    {
        while (x > 'Z')
        {
            x = x - 26;
        }
        return (char)x;
    }
    else
    {
        return (char)x;
    }
}
char cipher_lower(char a, int b)
{
    int x = a + b;
    if (x > 'z')
    {
        while (x > 'z')
        {
            x = x - 26;
        }
        return (char)x;
    }
    else
    {
        return (char)x;
    }
    return 1;
}