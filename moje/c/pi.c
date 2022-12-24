#include <stdio.h>
#include <string.h>
#include <time.h>

int main(void)
{
    double i = 1;
    double t = 0;
    char str[14];

    sprintf(str, "%.11f\r", t);
    clock_t start_time, end_time;
    start_time = clock();
    while (strcmp(str, "3.14159265358\r"))
    {
        for (int j = 0; j < 1000000; j++)
        {
            t += 4 / i;
            i += 2;
            t -= 4 / i;
            i += 2;
        }
        sprintf(str, "%.11f\r", t);
        printf("%s", str);
    }
    end_time = clock();
    printf("%f", i);
    printf("Time: %f", (double)(end_time - start_time) / CLOCKS_PER_SEC);

    return 0;
}
