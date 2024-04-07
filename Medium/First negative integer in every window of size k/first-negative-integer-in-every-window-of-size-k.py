#User function Template for python3

def printFirstNegativeInteger( arr, n, k):
    # code here
    ans = []
    i,j = 0, 0
    queue = []
    while (j < n):
        if (arr[j] < 0):
            queue.append(arr[j])
        if (j - i + 1 < k):
            j += 1
        elif (j - i + 1 == k):
            if (len(queue) == 0):
                ans.append(0)
            else:
                ans.append(queue[0])
            if (arr[i] < 0):
                queue.pop(0)
            i += 1
            j += 1
    return ans



#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        answer = printFirstNegativeInteger(a, n, k)
        for i in answer:
            print(i,end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends