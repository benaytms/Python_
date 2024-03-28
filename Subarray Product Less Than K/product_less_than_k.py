# Given an array of integers nums and an integer k, return the number of contiguous subarrays where the
# product of all the elements in the subarray is strictly less than k.
class Solution():
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k<=1:
            return 0
        # if K is 1 or 0, its not possible for any nums value to be valid because they can only be 
        # 1 or greater
        # and it can't be 1 because it has to be smaller than k, so it returns 0 as a default
        
        num_subarrays: int = 0
        # number of subarrays found
        left: int = 0
        # left pointer initialization
        product: int = 1
        # product initialization

        for i in range(len(nums)):
            # iterate through the array
            product *= nums[i]
            # multiplies the current number with the previous one
            while product >= k and left<=i:
                # if the product gets larger than K, and the left pointer is not ahead of the right one
                # the loop starts, and until the product is less than K it keeps dividing with the value
                # on the left pointer
                product //= nums[left]
                left += 1
                # moves the left pointer
            num_subarrays += (i - left + 1)
            # adds the number of subarrays (this operation can be clarified with the video on 
            # the last comment)
        return num_subarrays
        # returns the number of subarrays valid

# this problem can be solved with brute force but it occurs time extrapolation
# so for the solution is used the sliding window method.
# it works by having two pointers, the left one stays on 0 (first index), the right one moves iterating 
# every value on the array and multiplying
# them with each other. If it finds a product larger or equal to K, it divides the product with the value on
# the left pointer, if that makes the product smaller than K it keeps iterating, if not, the left pointer 
# keeps moving until it does. At the same, using the pointers, it calculates how many subarrays have been
# kept track of. Its quite difficult to explain the process but i recommend this vid: 
# https://www.youtube.com/watch?v=Cg6_nF7YIks - it really helped me understand this algorithm
