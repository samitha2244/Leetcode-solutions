class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count=0
        ans=[]


        for i in nums:
            count+=i
            ans.append(count)
        return ans    


        