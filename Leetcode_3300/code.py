class Solution:
    def minElement(self, nums: list[int]) -> int:
        list_1 = []
        for i in nums:
            sum_digits = 0
            while i > 0:
                n = i % 10
                i = i // 10
                sum_digits += n
            list_1.append(sum_digits)
        
        list_1.sort()  
        return list_1[0]  
