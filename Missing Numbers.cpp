// https://www.hackerrank.com/challenges/missing-numbers/problem


#include <bits/stdc++.h>

using namespace std;

vector <int> missingNumbers(vector <int> arr, vector <int> brr) {
    int a[10000]={0} , j=0 , b[10000]={0} ;
    vector <int> res(0) ;

    for(int i =0 ; i<brr.size() ; i++)
        b[brr[i]]++ ;
    for(int i =0 ; i<arr.size() ; i++)
        b[arr[i]]-- ;
    for(int i =0 ; i<arr.size() ; i++)
        if(b[arr[i]]>0) res.push_back(arr[i]) ;

   sort( res.begin(), res.end() );
   res.erase( unique( res.begin(), res.end() ), res.end() );

    return res ;

}


int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for(int arr_i = 0; arr_i < n; arr_i++){
       cin >> arr[arr_i];
    }
    int m;
    cin >> m;
    vector<int> brr(m);
    for(int brr_i = 0; brr_i < m; brr_i++){
       cin >> brr[brr_i];
    }
    vector <int> result = missingNumbers(arr, brr);
    for (ssize_t i = 0; i < result.size(); i++) {
        cout << result[i] << (i != result.size() - 1 ? " " : "");
    }
    cout << endl;


    return 0;
}
