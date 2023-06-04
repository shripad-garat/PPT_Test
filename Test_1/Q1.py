"""
Move Zeroes
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
a. 1 <= nums.length <= 10^4
b. -2^31 <= nums[i] <= 2^31 - 1

Note: Create a GitHub file for the solution and add the file link the the answer section below.
"""

def MoveZero(arr):
    try:
        l = 0
        r = len(arr) - 1
        if r == 0:
            return arr
        
        for i in range(len(arr)):
            while arr[l]!=0:
                l+=1
            if arr[i]!=0:
                arr[l] = arr[i]
                arr[i] = 0
            
        return arr     

    except Exception as e:
        raise e
    

nums = [0,1,0,3,12]
print(MoveZero(nums))