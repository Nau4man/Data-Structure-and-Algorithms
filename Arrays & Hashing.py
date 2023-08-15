class Solution:

#self: This suggests that the function is intended to be part of a class and can access the class's 
# attributes and methods through the self parameter. This is a common convention in object-oriented 
# programming in Python.

#nums: List[int]: This specifies that the parameter nums should be a list of integers (int). 
# The colon : is used to annotate the parameter with its expected type.

#-> bool: This indicates that the return value of the function is expected to be a boolean (bool).

    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()  # Create an empty set called 'hashset' to store unique elements

        for n in nums:   # Iterate through each element 'n' in the input list 'nums'
            if n in hashset:  # Check if the current element 'n' is already in the 'hashset'
                return True    # If 'n' is found in 'hashset', it's a duplicate, so return True
            hashset.add(n)    # If 'n' is not in 'hashset', add it to the set
        
        return False   # If the loop completes without finding any duplicates, return False

    
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if the lengths of the input strings are different
        if len(s) != len(t):
            return False  # If lengths are different, they can't be anagrams

        # Initialize dictionaries to count character frequencies in each string
        countS, countT = {}, {}

        # Iterate through the characters in the strings
        for i in range(len(s)):
            # For string 's':
            # Increment the count of the current character by 1 if it's already in the dictionary,
            # otherwise set its count to 1.
            countS[s[i]] = 1 + countS.get(s[i], 0)
            
            # For string 't':
            # Increment the count of the current character by 1 if it's already in the dictionary,
            # otherwise set its count to 1.
            countT[t[i]] = 1 + countT.get(t[i], 0)
            
        # Compare the two dictionaries to check if character frequencies match
        return countS == countT

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store previously encountered values as keys and their indices as values
        prevMap = {}  # val -> index

        # Iterate through the list of numbers along with their indices
        for i, n in enumerate(nums):
            # Calculate the difference between the target value and the current number
            diff = target - n
            
            # Check if the difference (complement) exists in the prevMap dictionary
            if diff in prevMap:
                # If the difference is found in prevMap, it means we have found a pair of indices
                # whose corresponding values add up to the target
                # Return the indices of the current number and the one in prevMap
                return [prevMap[diff], i]
            
            # If the difference is not in prevMap, add the current number to prevMap with its index
            prevMap[n] = i

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Create a defaultdict to store anagrams as values grouped by their character count tuple as keys
        ans = collections.defaultdict(list)

        # Iterate through the list of input strings
        for s in strs:
            # Initialize a list 'count' to store the frequency of characters (a-z) in the current string
            count = [0] * 26
            
            # Iterate through each character 'c' in the current string 's'
            for c in s:
                # Increment the count of the corresponding character's position in the 'count' list
                count[ord(c) - ord("a")] += 1
            
            # Convert the 'count' list into a tuple so it can be used as a dictionary key
            # Add the current string 's' to the list associated with the tuple key in 'ans'
            ans[tuple(count)].append(s)
        
        # Return the grouped anagrams as a list of lists (values of the 'ans' dictionary)
        return ans.values()

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to store the frequency of each number in 'nums'
        count = {}
        # Create a list of lists 'freq', where each sublist will contain numbers with the same frequency
        freq = [[] for i in range(len(nums) + 1)]

        # Count the frequency of each number in 'nums' and store it in the 'count' dictionary
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        # Populate the 'freq' list of lists with numbers grouped by their frequencies
        for n, c in count.items():
            freq[c].append(n)

        # Initialize the result list to store the top k frequent numbers
        res = []

        # Iterate through the 'freq' list in reverse order (higher frequencies first)
        for i in range(len(freq) - 1, 0, -1):
            # Iterate through the numbers in the current frequency group
            for n in freq[i]:
                # Append the number to the 'res' list
                res.append(n)
                # Check if the desired k elements have been found
                if len(res) == k:
                    return res  # Return the result list when k elements are collected





solution_instance = Solution()


result  = solution_instance.containsDuplicate([1,2,3,1])
print(result)

