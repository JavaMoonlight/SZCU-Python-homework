# Implement the insertion sort algorithm
def insertionSort(nums):
    for i in range(len(nums)):
        while nums[i-1] > nums[i] and (i-1) >= 0:
            nums[i-1],nums[i] = nums[i],nums[i-1]
            i -= 1
    return nums

# Main running function
def main():
    nums = [1,5,3,9,45,20,10,17,50,7,30]
    result = insertionSort(nums)
    print(result)

main()