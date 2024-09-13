#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv)
{
    int max_value = atoi(argv[1]);
    int i = 1;
    int result = 1;
    while (i <= max_value)
    {
        if (result % i == 0)
        {
            if (i == max_value)
            {
                printf("%d\n",result);
                return 0;
            }
            i++;
        }

        else
        {
            result++;
            i = 1;

        }

    }
    return 0;
}
