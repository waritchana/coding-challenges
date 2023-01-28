class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Choose to use two pointers from the beginning and the last
        # since the list is sorted
        i = 0
        j = len(numbers)-1

        while i < j:
            two_sum = numbers[i] + numbers[j]
            # Move left pointer to move value if less than target
            if two_sum < target:
                i += 1
            # Move right pointer to lower value if exceeds target
            elif two_sum > target:
                j -= 1
            elif two_sum == target:
                return [i+1, j+1]
