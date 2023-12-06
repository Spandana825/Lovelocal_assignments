def ele_occurring_morethan(nums):
    if not nums:
        return []
    #checks whether the list is empty,if empty returns empty list

  
    majority1, majority2, count1, count2 = 0, 1, 0, 0
    #variables of two elements and their count
    # First pass: Find majority elements and updates their count
    for num in nums:
        if num == majority1:
            count1 += 1
        elif num == majority2:
            count2 += 1
        elif count1 == 0:
            majority1, count1 = num, 1
        elif count2 == 0:
            majority2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Second pass: Count occurrences of majority elements in the list
    count1, count2 = 0, 0
    for num in nums:
        if num == majority1:
            count1 += 1
        elif num == majority2:
            count2 += 1

    # Check majority elements that appear more than n/3 times
    result = []
    if count1 > len(nums) // 3:
        result.append(majority1)
    if count2 > len(nums) // 3:
        result.append(majority2)

    return result

# Taking input from the user and converting it to list
nums_str = input("Enter the integers separated by spaces: ")
nums = list(map(int, nums_str.split()))

# Call the function with user input
result = ele_occurring_morethan(nums)
print("Elements appearing more than n/3 times:", result)
