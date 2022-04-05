// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;


 // } Driver Code Ends
// ranges[i][0] is the start of ith range
class Solution{
public:
    static bool sortbysec(const vector<int> &a,const vector<int> &b)
    {
        return (a[1] < b[1]);
    }
    int max_non_overlapping( vector< vector<int> >& ranges )
    {
        // it is a greedy approach that is already solved actually 
        // in gfg it is called N meetins in one room so go there and solve that 
        // these types of questions then you can easily solve
        
        
        //sort by second element first of all
        sort(ranges.begin(),ranges.end(),sortbysec);
        //now take two pointers and compare the results
        int f1=0,f2=0,count=0;
        while(f2<ranges.size())
        {
            if(ranges[f2][0]>=ranges[f1][1])//as per the question include the equals to sign also
            {
                f1=f2;
                count++;
            }    
            f2++;
        }
        //+1 is for the last element
        return count+1;
    }
};

// { Driver Code Starts.

int main()
{
	int t;
	cin>>t;
	while(t--)
	{
		int n;
		cin>>n;

		vector< vector<int> > v(n,vector<int>(2));
		for(int i=0; i<n; i++)
			cin>> v[i][0] >> v[i][1];
			
        Solution ob;
		cout<< ob.max_non_overlapping(v) << endl;
	}
	return 1;
}

  // } Driver Code Ends