#include <bits/stdc++.h>
#include <iostream>

using namespace std;

int main()
{
    int a,b,count=0;
    cin >> a >>b;

    while (a<b)
    {
        a=3a;
        b=2b;
        count++;
    }

    cout <<""<< count;
    

    return 0;
}
