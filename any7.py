def any7(nums):
    target=7
    for num in nums:
        if num == target :
            return  True
    return False
    # YOUR CODE HERE 

print("should be true", any7([1, 2, 7, 4, 5]))
print("should be false", any7([1, 2, 4, 5]))
