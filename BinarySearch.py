import time

def binarySearch(nums, key):
    low = 0
    high = len(nums) - 1
    while low <= high:
         mid = int((low+high)/2)
         if key == nums[mid]:
             return mid
         if key > nums[mid]:
             low = mid + 1
         else:
             high = mid - 1
    return -1

def printTime(N, key):
    numbers = list(range(N+1))
    print('key값 : ', key, sep='')
    start = time.time()
    result = binarySearch(numbers, key)
    end = time.time() - start
    print('데이터의 개수 : %d, 실행시간 : %f, 위치 : %d'%(N, end, result))

import random

key = random.randint(1,1000)
printTime(1000,key)
key = random.randint(1,1000)
printTime(10000,key)
key = random.randint(1,1000)
printTime(100000,key)
key = random.randint(1,1000)
printTime(1000000,key)