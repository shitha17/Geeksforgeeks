#User function Template for python3
class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        i,sub_sum,ans = 0,0,0,
        
        for j in range(N):
            sub_sum += Arr[j]
            if j-i+1 == K:
                ans = max (ans,sub_sum)
                sub_sum -= Arr[i]
                i+=1
                j+=1
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        N,K = input().split()
        N = int(N)
        K = int(K)
        Arr = list( map(int,input().strip().split(" ")))

        ob = Solution()
        print(ob.maximumSumSubarray(K,Arr,N))
# } Driver Code Ends