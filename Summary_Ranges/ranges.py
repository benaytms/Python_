def summaryRanges(nums: list[int]) -> list[str]:
    if not nums:
        return []

    n = len(nums)
    ranges = []
    start = nums[0]

    for i in range(1, n):
        if (nums[i]-1 != nums[i-1]):
            if start == nums[i-1]:
                # in case there's only one value
                ranges.append(str(start))
            else:
                ranges.append(str(start) + "->" + str(nums[i-1]))
            start = nums[i]
        else:
            pass
    
    if start == nums[-1]:
        ranges.append(str(start))
    else:
        ranges.append(str(start) + "->" + str(nums[-1]))

    return ranges

if __name__ == "__main__":
    testlist = [0, 2, 3, 5, 8, 9, 10, 11, 26, 27, -4, -3, -2, 5]
    print(summaryRanges(testlist))
