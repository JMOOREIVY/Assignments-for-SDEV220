#James Moore
#SDEV220-50P Module 3 Tutorial (Binary Search)
class Solution:
    def binarysearch(self, arr, k):
        low = 0
        high = len(arr) - 1
        result = -1
        
        while low <= high:
            mid = low + (high - low) // 2
            
            if arr[mid] == k:
                result = mid      # Record the index
                high = mid - 1    # Keep looking left for the first occurrence
            elif arr[mid] < k:
                low = mid + 1
            else:
                high = mid - 1
                
        return result