class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        _sum = 0
        mymap = {0: 0}  # {sum: pos}

        for i in range(n):
            _sum += nums[i]
            mymap[_sum] = i

        if x > _sum:  # Sum out of range
            return -1

        mymap[0] = 0

        longest = 0
        _sum -= x
        val = 0

        for i in range(n):
            val += nums[i]
            if val - _sum in mymap:
                if val - _sum == 0:
                    longest = max(longest, i - mymap[val - _sum] + 1)
                else:
                    longest = max(longest, i - mymap[val - _sum])

        return n - longest if longest != 0 else (n if _sum == 0 else -1)
