from asyncio.windows_events import NULL


def twoSum( nums, target):
    for i in range(len(nums)):
        if nums[i] + nums[i + 1]:
            return [i, i + 1]
    return NULL    

print(twoSum([2,7,11,15], 9))        