class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique = set()

        for n in nums:
            if n in unique:
                return True
            unique.add(n) # so to add element to set have to .add(element)
        
        return False
