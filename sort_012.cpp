#include <bits/stdc++.h>
using namespace std;

int main()
{
    int n;
    cin >> n;

    int arr[n], zero = 0, one = 0;
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
        if (arr[i] == 0)
            zero++;
        else if (arr[i] == 1)
            one++;
    }
    int two = n - zero - one, i = 0;
    while (zero--)
    {
        arr[i] = 0;
        i++;
    }
    while (one--)
    {
        arr[i] = 1;
        i++;
    }
    while (two--)
    {
        arr[i] = 2;
        i++;
    }

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}