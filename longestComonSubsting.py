from typing import List

def longest_common_prefix(arr: List[str]) -> str:
    if not arr:
        return ""  # Handle empty list case
    
    # Start with the first string as the prefix
    prefix = arr[0]
    
    for string in arr[1:]:
        # Find the minimum length between the prefix and the current string
        while not string.startswith(prefix):
            prefix = prefix[:-1]  # Shorten the prefix
            
            if not prefix:
                return ""  # No common prefix
    
    return prefix

# Example Usage
arr = ["geeksforgeeks", "geeks", "geek", "geezer"]
print(longest_common_prefix(arr))  # Output: "gee"
