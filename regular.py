from ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int):
        self.n=list(map(int,nums.split()))
        self.t= target

    def result(self):
        print(self.n[1]+self.n[0])
