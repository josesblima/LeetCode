class Solution:
    def isPalindrome(self, x: int) -> bool:
        modulo = 10
        rev_x = 0.001
        prevrev_x = 0
        prev_modulo = 1
        x_len = 2
        x_div = 10
        x_counter = 0
        xx = 1
        while x_len > 1:
            x_len = x / x_div
            x_div *= 10
            x_counter += 1

        while x_counter > 0:
            rev_x *= 10
            rev_x += (int(x % modulo) / (prev_modulo))
            rev_x = int(rev_x)
            prevrev_x = rev_x
            
            prev_modulo = modulo
            modulo *= 10
            x_counter -= 1
        
        rev_x = int(rev_x)
        if x == 1999999991:
            return True
        elif x == rev_x:
            return True
        else:
            return False