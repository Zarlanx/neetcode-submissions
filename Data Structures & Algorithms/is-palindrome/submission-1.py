class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0

        new_string = (''.join([char for char in s if char.isalnum()])).lower()
        r = (len(new_string) - 1)    
        while l <= r:
            print(new_string[l])
            if len(s) == 0 or len(s) == 1:
                return True
            elif new_string[l] == new_string[r]:
                l += 1
                r -= 1
            else:
                return False
        return True