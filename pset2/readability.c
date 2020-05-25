#include<cs50.h>
#include <stdio.h>
#include<string.h>
#include<ctype.h>
int rounda(double x); // round fn for index
int letter_count(string str); // to count letter in string
int word_count(string str); // to count the word in the string
int sentance_count(string str); // to calc how many sentance in string

int main(void)
{
    float letter, word, sentance, out;
    int y;
    double index;
    string name = get_string("What's the text?\n");
    letter = letter_count(name);
    word = word_count(name);
    sentance = sentance_count(name);
    index = (0.0588 * ((letter / word) * 100) - 0.296 * ((sentance / word) * 100) - 15.8);
    y = rounda(index);
    if (y < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (y > 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %d\n", y);
    }

}

int rounda(double x)
{
    if (x < 0.0)
    {
        return (int)(x - 0.5);
    }
    else
    {
        return (int)(x + 0.5);
    }
}


int sentance_count(string str)
{
    int counter = 0;
    for (int i = 0 ; i < strlen(str) ; i++)
    {
        if (str[i] == '?' || str[i] == '!' || str[i] == '.')
        {
            counter++;
        }
    }
    return counter;
}
int word_count(string str)
{
    int counter = 0;
    for (int i = 0 ; i < strlen(str) ; i++)
    {
        if (str[i] == ' ')
        {
            counter++;
        }
    }
    return counter + 1;
}
int letter_count(string str)
{
    int counter = 0;
    for (int i = 0 ; i < strlen(str) ; i++)
    {
        if ((isalpha(str[i])) || (isalnum(str[i])))
        {
            counter++;
        }
    }
    return counter;
}