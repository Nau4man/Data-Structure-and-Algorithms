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


solution_instance = Solution()


result  = solution_instance.containsDuplicate([1,2,3,1])
print(result)