
    
from re import S


def maximumProduct(nums):
    nums.sort()

    n = len(nums)
    max_product1 = nums[-1] * nums[-2] * nums[-3]  # All element of the list are positive or negative .
    max_product2 = nums[0] * nums[1] * nums[-1]    # first two elements are positive 

    return max(max_product1, max_product2)

