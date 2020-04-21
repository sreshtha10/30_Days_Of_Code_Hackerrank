#include<stdio.h>
int main()
{
    long int n,count = 0,max_count=0,c;
    scanf("%ld",&n);
    int a[1000] = {0}; 
    for(long int i = 0;n!=0;i++,count++)
    {   
        a[i] = n%2;
        n = n/2;
    }
    for(long int i = 0;i<count;i++)
    {
        c= 1;   
        if(a[i] != 1)
        {
            continue;
        }
        for(long int j=i+1;j<count;j++)
        {
            if(a[i] == a[j])
            {
                c++;
            }
            else{
                break;
            }
        }
        if(c>max_count)
        {
            max_count = c;
        }
    }
    printf("%ld",max_count);
    
}
