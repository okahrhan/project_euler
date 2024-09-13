#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    int value = atoi(argv[1]);
    int i = 1;
    int squares;
    int sum_squares;
    int result;

    while (i <= value)
    {
        squares += i*i;
        sum_squares += i;
        i++;
    }
    result = sum_squares*sum_squares - squares;
    printf("%d\n", result);


    return 0;
}