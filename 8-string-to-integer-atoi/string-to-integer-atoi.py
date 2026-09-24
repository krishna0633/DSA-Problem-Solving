class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)

        while i < n and s[i] == ' ':
            i += 1

        sign = 1

        if i < n and s[i] == '-':
            sign = -1
            i += 1
        elif i < n and s[i] == '+':
            i += 1

        result = 0

        while i < n and '0' <= s[i] <= '9':
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1

        result = result * sign

        if result < -2147483648:
            return -2147483648

        if result > 2147483647:
            return 2147483647

        return result