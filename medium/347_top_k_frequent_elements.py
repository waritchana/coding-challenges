from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use sorted lists
        hashmap = {}
        # Create a dictionary of the number and its occurance
        for num in nums:
            if num in hashmap.keys():
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        # Sort dictionary by max occurance (value)
        sorted_max = reversed(sorted(hashmap.values()))
        # Create lists of numbers and their occurances
        # to be referred to by index
        key_list = list(hashmap.keys())
        val_list = list(hashmap.values())
        result = []
        for count in sorted_max:
            if k > 0:
                position = val_list.index(count)
                result.append(key_list[position])
                # Remove after added to result to avoid get adding again
                key_list.pop(position)
                val_list.pop(position)
                k -= 1
        return result
        """
        # Use heap
        hashmap = {}
        for num in nums:
            if num in hashmap.keys():
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        heap = []
        for number, freq in hashmap.items():
            # In heap, every parent node has a value less than or equal
            # to any of its children
            # To have the most count numbers on the top,
            # set them to be the least number
            heap.append((-freq, number))
        # Transform a list to heap
        heapq.heapify(heap)
        result = []
        for tuple_item in range(k):
            # Return the top item of the heap and update the heap
            freq, number = heapq.heappop(heap)
            result.append(number)
        return result
        """
        """
        # Use bucket - O(n) memory and time
        hashmap = {}
        for num in nums:
            if num in hashmap.keys():
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        bucket_list = [[] for _ in range(len(nums)+1)]
        for number, freq in hashmap.items():
            bucket_list[freq-1].append(number)
        result = []
        for bucket in reversed(bucket_list):
            if len(bucket) > 0:
                for number in bucket:
                    if len(result) < k:
                        result.append(number)
                    else:
                        break
        return result
        """

nums = [1,1,1,2,2,3]
k = 2
# expected_output = [1, 2]

#nums = [1]
#k = 1
# expected_output = [1]
