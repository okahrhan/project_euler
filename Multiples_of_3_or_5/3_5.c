#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    if (argc != 2)
    {
        printf(" ERROR ", argv[0]);
        return 1;

    }

    int i = 0;
    int bellow = atoi(argv[1]);
    int sum = 0;

    while (i <= bellow)
    {
        if (i % 3 == 0 || i % 5 == 0)
        {
            sum += i;
        }
        i++;
    }
    printf("%d\n",sum);
}
