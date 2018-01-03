#include <bits/stdc++.h>

using namespace std;

int pairs(int k, vector <int> arr) {
    // Complete this function
    int diff , count = 0  ,i=0 , j =1 ;
    while(i<=j && j<=arr.size())
    {
        diff = arr[j]-arr[i] ;
        if(diff<k)
            j++ ;
        else if(diff>k)
            i++ ;
        else
        {
            count++ ;
            i++ ;
        }
    }

    return count;
}

int main() {
    int n;
    int k , temp , i ;
    cin >> n >> k;
    vector<int> arr(n);
    for(int arr_i = 0; arr_i < n; arr_i++){
       cin >>arr[arr_i] ;
    }
    sort(arr.begin() , arr.end() ) ;

    int result = pairs(k, arr);
    cout << result << endl;
    return 0;
}
