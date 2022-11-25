a = []
class Solution:
    def minSum(self, arr, n):
        arr_1 = 0
        arr_2 = 0

        for i in arr:
            a.append(i)

       
        a.sort()
        
        '''Sorted Array Result Displayed Successfully'''
        '''Time for the main logic for min sum'''

        for i in range(n):
            if i % 2 == 0:
                arr_1 = arr_1 * 10 + a[i]

            else:
                arr_2 = arr_2 * 10 + a[i]

        return arr_1 + arr_2
    


#{ 
 # Driver Code Starts

import heapq as hq

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        n = int(input())
        arr = [int(x) for x in input().split()]
        ob=Solution()
        print(ob.minSum(arr,n))

# } Driver Code Ends