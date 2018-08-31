#include <bits/stdc++.h>
// https://www.hackerrank.com/contests/world-codesprint-13/challenges/find-the-absent-students/problem
using namespace std;

vector<string> split_string(string);

// Complete the findTheAbsentStudents function below.
vector<int> findTheAbsentStudents(int n, vector<int> a) {
    // Return the list of student IDs of the missing students in increasing order.
    vector<int>r ; 
    sort(a.begin() , a.end()) ;
    for(int i =1 ; i<=a.size() ; i++)
    {
        if (!binary_search(a.begin()  , a.end() , 1 ))
            r.push_back(i) ; 
    }
    return r ; 
}

int main()
{

    int n;
    cin >> n;

    vector<int> a(n);

    for (int i = 0; i < n; i++) {
        cin>>a[i] ;
    }

    vector<int> result = findTheAbsentStudents(n, a);

    for (int i = 0; i < result.size(); i++) {
        cout << result[i];
        if (i != result.size() - 1) {
            cout << " ";
        }
    }
    cout<<endl; 

    return 0;
}

vector<string> split_string(string input_string) {
    string::iterator new_end = unique(input_string.begin(), input_string.end(), [] (const char &x, const char &y) {
        return x == y and x == ' ';
    });

    input_string.erase(new_end, input_string.end());

    while (input_string[input_string.length() - 1] == ' ') {
        input_string.pop_back();
    }

    vector<string> splits;
    char delimiter = ' ';

    size_t i = 0;
    size_t pos = input_string.find(delimiter);

    while (pos != string::npos) {
        splits.push_back(input_string.substr(i, pos - i));

        i = pos + 1;
        pos = input_string.find(delimiter, i);
    }

    splits.push_back(input_string.substr(i, min(pos, input_string.length()) - i + 1));

    return splits;
}
