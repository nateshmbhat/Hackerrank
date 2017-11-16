//https://www.hackerrank.com/contests/w35/challenges/triple-recursion/problem

#include <bits/stdc++.h>

using namespace std;
int a[100][100] ;

void tripleRecursion(int n, int m, int k) {
    // Complete this function
    if(n==1) return ; 
    int i , j ; 
    for(i=0 ; i<n ; i++)
        for(j=0 ; j<n ; j++)
        {
            if(i==0 && j==0 ) a[i][j] =m ; 
            else if(i==j) a[i][j] = a[i-1][j-1]+k ;
            else if (i>j) a[i][j] = a[i-1][j]-1;
            else if(i<j) a[i][j] = a[i][j-1]-1 ;
        }
    
}

int main() {
    int n;
    int m;
    int k;
    cin >> n >> m >> k;
    tripleRecursion(n, m, k);
    int i , j ; 
    for(i=0 ; i<n ; i++)
    {
        for(j=0 ; j<n ; j++)
            cout<<a[i][j]<<" " ;
        cout<<endl ;
    }
    return 0;
}
