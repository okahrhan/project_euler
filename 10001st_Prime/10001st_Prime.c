#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>


bool isPrime(int num)
{
    if (num <= 1) return false;
    if (num <= 3) return true;
    if (num % 2 == 0 || num % 3 == 0) return false;
    for (int i = 5; i * i <= num; i += 6)
    {
        if (num % i == 0 || num % (i + 2) == 0) return false;
    }
    return true;
}

int main(int argc, char **argv)
{
    int count = 0;
    int number = 1;
    int target = atoi(argv[1]);

    while (count < target)
    {
        number++;
        if (isPrime(number))
        {
            count++;
        }
    }

    printf("%d\n", number);

    return 0;
}
