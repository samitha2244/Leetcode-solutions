class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        cleaned = ""

        for ch in s:
            if ch.isalnum():
                cleaned += ch

        reverse = cleaned[::-1]

        if reverse == cleaned:
            return True
        return False    



        