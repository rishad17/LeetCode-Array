class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        for i in range(len(digits) - 1, -1, -1):  
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  
        return [1] + digits
    

            
        
sol = Solution()
print(sol.plusOne([4,3,2,2]))
