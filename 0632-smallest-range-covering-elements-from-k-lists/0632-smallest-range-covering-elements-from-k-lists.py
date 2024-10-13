import heapq

class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        min_heap = []
        current_max = float('-inf')
        for i in range(len(nums)):
            heapq.heappush(min_heap, (nums[i][0], i, 0))
            current_max = max(current_max, nums[i][0])

        best_range = [float('-inf'), float('inf')]  # (start, end)

        while True:
            current_min, list_index, element_index = heapq.heappop(min_heap)

            # Update the best range if the current range is smaller
            if current_max - current_min < best_range[1] - best_range[0] or \
               (current_max - current_min == best_range[1] - best_range[0] and current_min < best_range[0]):
                best_range = [current_min, current_max]

            # If we can move to the next element in the same list, do it
            if element_index + 1 < len(nums[list_index]):
                next_element = nums[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_element, list_index, element_index + 1))
                current_max = max(current_max, next_element)
            else:
                # If we reached the end of any list, we cannot continue
                break

        return best_range