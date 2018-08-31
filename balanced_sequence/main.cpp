#include <bits/stdc++.h>
// https://www.hackerrank.com/contests/world-codesprint-13/challenges/balanced-sequence/

using namespace std;

// Complete the fewestOperationsToBalance function below.
int fewestOperationsToBalance(string s) {
    // Return the minimum number of steps to make s balanced.
    int ans =0 ; unordered_map<char , char> pair ; 
    pair['('] = ')'  ; pair[')'] = '(' ; 

    stack<char> stk ; 

    for(char c : s)
    {
        if(c=='(') stk.push(c) ;
        else if (c==')' && stk.empty())
            stk.push(c);
        else if(c==')' && stk.top()=='(')
            stk.pop() ;
        else
            stk.push(c) ; 
    }

    char temp ='#'  ;
    while(!stk.empty())
    { 
        if(stk.top()!=temp){
            temp = stk.top() ;
            ans+=1  ; 
        }
        stk.pop() ; 
    }

    return ans ; 
}

int main()
{
    // ofstream cout(getenv("OUTPUT_PATH"));

    int n;
    cin >> n;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    string s;
    getline(cin, s);

    int result = fewestOperationsToBalance(s);

    cout << result << "\n";

    return 0;
}
