// egyszerű aritmetikai művelet (szorzás)

#include <stdio.h>

int main()
{
    // float (valós, lebegőpontos) érték beolvasása
    float ar;
    printf("Ar AFA nelkul?\n");
    scanf("%f", &ar);

    float total = ar * 1.27;
    printf("Teljes ar: %f\n", total);

    return 0;
}
