#include<bits/stdc++.h>
using namespace std;
void bubbleSort(int a[],int n){
    int k = 0;
    int no_swap = 0;
    for(k=0;k<n;k++){
        for(int i=0;i<n-k-1;i++){
            if(a[i]>a[i+1])
            {
                no_swap++;
                swap(a[i],a[i+1]);
               
            }
        }
   
      
    }
    cout<<"Max no of swaps  : "<<endl;
    cout<<no_swap<<endl;
    
}
int main(){
    int n;
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++){
        cin>>a[i];
    }
    bubbleSort(a,n);
    for(int i=0;i<n;i++){
        cout<<a[i]<<" ";
    }
}
