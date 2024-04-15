#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) : 
        map = {}
        sum = 0
        len = 0

        for i in range(n):
            sum += arr[i]

            if sum == k:
                len = max(len, i + 1)

            if sum - k in map:
                len = max(len, i - map[sum - k])

            if sum not in map:
                map[sum] = i

        return len
        #Complete the function
    





            
            
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends