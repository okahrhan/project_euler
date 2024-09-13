#include <math.h>
#include <stdio.h>
#include <stdlib.h>

long long maxPrimeFactors(long long n) {
    long long maxPrime = -1;

    while (n % 2 == 0) {
        maxPrime = 2;
        n >>= 1;
    }

    while (n % 3 == 0) {
        maxPrime = 3;
        n = n / 3;
    }

    int i = 5;
    while (i * i <= n) {
        while (n % i == 0) {
            maxPrime = i;
            n = n / i;
        }
        while (n % (i + 2) == 0) {
            maxPrime = i + 2;
            n = n / (i + 2);
        }
        i += 6;
    }

    if (n > 4)
        maxPrime = n;

    return maxPrime;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        printf("Usage: %s <number>\n", argv[0]);
        return 1;
    }

    long long n = atoll(argv[1]);
    printf("%lld\n", maxPrimeFactors(n));

    return 0;
}
