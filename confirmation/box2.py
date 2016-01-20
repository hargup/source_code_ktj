#!/usr/bin/python
try:
    input = raw_input
except NameError:
    pass


def rule(nums):
    diffs = map(lambda x, y: y-x, nums[:-1], nums[1:])
    if min(diffs) > 0:
        return True
    else:
        return False

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    print(rule(nums))
