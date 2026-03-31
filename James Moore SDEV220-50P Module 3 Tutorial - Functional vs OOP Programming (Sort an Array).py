#James Moore
#SDEV220-50P Module 3 Tutorial (Sort an Array)
class Solution:
    def sort012(self, arr):    #creates the array, using low, mid, and high to organize the input
        low = 0 
        mid = 0
        high = len(arr) - 1

        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            elif arr[mid] == 1:
                mid += 1
            else: # arr[mid] == 2
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
        
        return arr # Return after the loop finishes