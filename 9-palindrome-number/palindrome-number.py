class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s=str(x)
        reverse=s[::-1]
        if reverse==s:
            return True
        return False     

        