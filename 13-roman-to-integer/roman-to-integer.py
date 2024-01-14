class Solution:
    def romanToInt(self, s: str) -> int:
        finalcount = 0
        roman_dic = {
        'I' : 1,
        'V' : 5,
        'X' : 10,
        'L' : 50,
        'C' : 100,
        'D' : 500,
        'M' : 1000
        }
        prev_num = None
        for num in s:
            if prev_num == 'I' and num == 'V':
                finalcount += 3
            elif prev_num == 'I' and num == 'X':
                finalcount += 8
            elif prev_num == 'X' and num == 'L':
                finalcount += 30
            elif prev_num == 'X' and num == 'C':
                finalcount += 80
            elif prev_num == 'C' and num == 'D':
                finalcount += 300
            elif prev_num == 'C' and num == 'M':
                finalcount += 800
            else:
                finalcount += roman_dic[num]
            prev_num = num   
        return finalcount
