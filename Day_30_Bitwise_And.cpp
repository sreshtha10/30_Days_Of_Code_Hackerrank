#include <iostream>
using namespace std;

int main()
{
    int t,n,k,max;
    cin >> t;    
    while(t>0)
    {
        cin >> n >> k;
        max = 0;
        for(int i = 1;i<n;i++)
        {
            for(int j = i+1;j<=n;j++)
            {
                if((i&j) > max && (i&j) < k && i<j)
                {
                    max = i&j;
                }
            }
        }
        cout << max << endl;
        t--;
    }
 
}
