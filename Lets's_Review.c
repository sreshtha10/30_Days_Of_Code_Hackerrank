#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int main() {

    int t;
    scanf("%d",&t);
    char s[10000];
    for(int i = 0;i<t;i++)
    {
        scanf("%s",s);
        for(int j = 0;j<strlen(s);j++)
        {
            if((j%2 == 0))
            {
                printf("%c",s[j]);
            }
        }
        printf("%c",32);
        for (int k = 0;k<strlen(s);k++) {
            if(k%2 != 0)
            {
                printf("%c",s[k]);
            }
        }
        printf("\n");
    }
    return 0;
}
