from collections import deque
class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        dq.append(0)
        l, r = 0, 1
        res = []
        if k == 1 or len(nums) == 1:
            return nums
        while r < len(nums):
            while len(dq) > 0 and nums[dq[-1]] <= nums[r]:
                dq.pop()
            dq.append(r)
            if r - l < k - 1:
                r += 1
                continue
            if r - l == k - 1:
                while dq[0] < l:
                    dq.popleft()
                res.append(nums[dq[0]])
                l += 1; r += 1
                continue
        return res
    maxSlidingWindow(1, nums = [1,3,1,2,0,5], k = 3)