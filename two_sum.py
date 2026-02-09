## problem no: 1 -- two sum 

def twosum_linear_search(list, target):
    """Find two indices where the values sum to target using nested loop (brute force).
    
    Args:
        list: List of integers to search
        target: Target sum value
        
    Returns:
        List containing indices [i, j] where list[i] + list[j] == target, or None if not found
        
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    for i in range(len(list)):
        for j in range(i+1, len(list)):
            if(list[i] + list[j] == target):
                return [i,j]



def twosum_need_search(list, target):
    """Find two indices where the values sum to target using the 'need' complement approach.
    
    Args:
        list: List of integers to search
        target: Target sum value
        
    Returns:
        List containing indices [i, j] where list[i] + list[j] == target, or None if not found
        
    Time Complexity: O(n^2) due to list.index() calls
    Space Complexity: O(1)
    """
    for i in range(len(list)):
        need = target - list[i]
        if(need in list and list.index(need) != i):
                return [i,list.index(need)]



def twosum_with_dict(list, target):
    """Find two indices where the values sum to target using a dictionary for fast lookups.
    
    Args:
        list: List of integers to search
        target: Target sum value
        
    Returns:
        List containing indices [i, j] where list[i] + list[j] == target, or None if not found
        
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    d = dict();
    for i in range(len(list)):
        d[list[i]] = i
    
    for i in range(len(list)):
        need = target - list[i]
        if(need in d.keys() and d[need] != i):
            return [i, d[need]]



print(twosum_linear_search([3,5,6,7,8,2], 10))
print(twosum_need_search([3,5,6,7,8,2], 10))
print(twosum_with_dict([3,5,6,7,8,2], 10))