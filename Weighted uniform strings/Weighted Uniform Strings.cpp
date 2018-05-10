#include <bits/stdc++.h>
#include<unordered_map>

using namespace std;

/*
 * Complete the weightedUniformStrings function below.
 */
vector<string> weightedUniformStrings(string s, vector<int> queries) {
    int runlength , tempweight =0 ;  
    vector<string> result ;
    unordered_set<int> hash ;
    
    for(int i =0 ; i<s.length() ; )
    {
        runlength = 1 ;
        tempweight = s[i]-'a'+1 ; 
        hash.insert(tempweight) ;
        
        while(runlength+i < s.length() && s[i+runlength] ==s[i])
        {
            runlength+=1 ;
            tempweight+= s[i]-'a'+1 ;            
            hash.insert(tempweight) ;
        }
        
        i+=runlength ; 
    }
    
    for(int i=0 ; i<queries.size() ; i++)
    {
        if(hash.find(queries[i])!=hash.end())
            result.push_back("Yes") ;
        else
            result.push_back("No") ; 
    }
    
    return result ; 

}

int main()
{
    ofstream fout(getenv("OUTPUT_PATH"));

    string s;
    getline(cin, s);

    int queries_count;
    cin >> queries_count;
    cin.ignore(numeric_limits<streamsize>::max(), '\n');

    vector<int> queries(queries_count);

    for (int queries_itr = 0; queries_itr < queries_count; queries_itr++) {
        int queries_item;
        cin >> queries_item;
        cin.ignore(numeric_limits<streamsize>::max(), '\n');

        queries[queries_itr] = queries_item;
    }

    vector<string> result = weightedUniformStrings(s, queries);

    for (int result_itr = 0; result_itr < result.size(); result_itr++) {
        fout << result[result_itr];

        if (result_itr != result.size() - 1) {
            fout << "\n";
        }
    }

    fout << "\n";

    fout.close();

    return 0;
}
