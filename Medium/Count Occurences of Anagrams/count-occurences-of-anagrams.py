#User function Template for python3
class Solution:

    
    def search(self,pat, txt):
        mp = {}
        ans = 0
        
        # Storing the occurrences of string p in the map
        for x in pat:
            mp[x] = mp.get(x, 0) + 1
    
        count = len(mp)
        k = len(pat)
        i = 0
        j = 0
    
        while j < len(txt):
            # Calculation part
            if txt[j] in mp:
                mp[txt[j]] -= 1
                if mp[txt[j]] == 0:
                    count -= 1
    
            # Window length not achieved yet
            if j - i + 1 < k:
                j += 1
    
            # Window length achieved, find answer and slide the window
            elif j - i + 1 == k:
                # Finding the answer
                if count == 0:
                    ans += 1
                if txt[i] in mp:
                    mp[txt[i]] += 1
                    if mp[txt[i]] == 1:
                        count += 1
    
                # Slide the window
                i += 1
                j += 1
    
        return ans

	           


#{ 
 # Driver Code Starts
#Initial Template for Python 3


# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        txt=input().strip()
        pat=input().strip()
        ob = Solution()
        ans = ob.search(pat, txt)
        print(ans)
        tc=tc-1
# } Driver Code Ends