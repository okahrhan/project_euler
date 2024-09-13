#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    int max_value = atoi(argv[1]);
    int i = 2;
    int j = 1;
    int sum = 0;
    while (i < max_value)
    {
        if (i % 2 == 0)
        {
            sum += i;
        }

        int next = i + j;
        j = i;
        i = next;
    }
    printf("%d\n",sum);
    return 0;
}
