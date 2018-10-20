class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not nums or k == 0:
            return []
        
        retlist = []
        # Get max in first sliding window
        cur_max = nums[0]
        max_index = 0
        start = 0
        end = k-1
        max_index, cur_max = self.getmax(0, k, nums, cur_max, max_index)
        
        retlist.append(cur_max)
        # Now move the sliding window 
        for i in range(k, len(nums)):
            start, end = start+1, end+1
            if nums[end] > cur_max:
                cur_max = nums[end]
                max_index = end
            # This is wrong
            elif start > max_index:
                max_index, cur_max = self.getmax(start, end+1, nums, nums[start], start)
            else:
                pass
            
            retlist.append(cur_max)
        return retlist

    def getmax(self, start, end, nums, cur_max, max_index):
        for i in range(start, end):
            if nums[i] > cur_max:
                cur_max = nums[i]
                max_index = i
        return max_index, cur_max

if __name__ == '__main__':
    s = Solution()
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    retval = s.maxSlidingWindow(nums, k)
    assert(retval == [3,3,5,5,6,7])
    assert(s.maxSlidingWindow([], 5) == [])
    assert(s.maxSlidingWindow([1, 2, 3], 0) == [])
