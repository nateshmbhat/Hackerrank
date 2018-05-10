#include <bits/stdc++.h>

using namespace std;


bool checkstring(string s)
{
    if(s.length()<2) return 0 ;
    if(s.length()==2) return 1;
    
    for(int i=2 , j=3 ; i<s.length() && j<s.length() ; i+=2 , j+=2 )
    {
        if(s[i]==s[j] || s[i]!=s[i-2] || s[j]!=s[j-2]  ) return 0 ;
    }
    
    if(s[s.length()-1]!=s[s.length()-3]) return 0 ;
    
    return true ; 
}

int twoCharaters(string s) {
    int ans  = 0  ;
    string temp ; 
    
    for(int i='a' ; i<'z' ; i++)
    {
        for(int j='a' ; j<'z' ; j++)
        {
            if(i==j) continue ; 
            temp = "" ; 
            for(int t=0 ; t<s.length() ; t++)
                if(s[t]==i || s[t]==j)
                    temp+=s[t] ;
            
            if(checkstring(temp))
                ans = max((int)temp.length() , ans) ;
        }
        
    }
    
    return ans ; 
    // Complete this function
}

int main() {
    int l;
    cin >> l;
    string s;
    cin >> s;
    int result = twoCharaters(s);
    cout << result << endl;
    return 0;
}
