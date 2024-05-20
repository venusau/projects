class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # Check for sign of dividend and divisor
        is_negative = (dividend < 0) ^ (divisor < 0)
        
        # Take absolute values of dividend and divisor
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        # Perform division
        quotient = 0
        while dividend >= divisor:
            dividend -= divisor
            quotient += 1
        
        # Adjust sign of quotient
        if is_negative:
            quotient = -quotient
        
        return min(max(-2**31, quotient), 2**31 - 1)  # Adjust result within range

# Taking input and calling the divide method
solution = Solution()
dividend = int(input("Enter the dividend :\n"))
divisor = int(input("Enter the divisor :\n"))
result = solution.divide(dividend, divisor)
print("Output:\n", result)
