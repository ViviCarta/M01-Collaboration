"""Author: Venise Saron
Professor: Ray Storer
Subject: SDEV 220
Last Revised: 2-4-2024
Module #: M03 Tutorial - Functional vs OOP Programming
Github URL: https://github.com/ViviCarta/M01-Collaboration.git
"""

# Sort an array of 0s, 1s and 2

class Solution:
    # Function to sort an array of 0s, 1s, and 2s.
    def sort012(self,arr,n):
        
        # Maintain 3 variables low, high and mid
        low = 0
        high = n-1
        mid = 0
        
        while mid <= high:
            
            if arr[mid] == 0:
                arr[mid], arr[low] = arr[low], arr[mid]
                mid += 1
                low +=1
              
            elif arr[mid] == 1:
                mid += 1
              
            else:
                arr[mid], arr[high], = arr[high], arr[mid]
                high -= 1
    



#{ 
 # Driver Code Starts

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends