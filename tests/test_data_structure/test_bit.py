from random import *
from data_structure.bit import *

class TestBIT_SUM():
    def test(self):
        #* 创建N个数组
        N = 100
        #* 每个数组测试K个操作
        K = 1000
        for _ in range(N):
            #* 创建长度为M的数组
            M = randint(100, 200)
            nums = [randint(1, 1000) for _ in range(M)]
            nums_copy = nums.copy()
            bit = BIT_SUM(nums)
            for _ in range(K):
                #* 0操作是更改, 1操作是查询
                op = randint(0, 1)
                if(op==0):
                    index = randint(0, M-1)
                    inc = randint(1, 100)
                    bit.inc(index, inc)
                    nums_copy[index] += inc
                else:
                    left = randint(0, M-2)
                    right = randint(left, M-1)
                    res = bit.query(left, right)
                    ans = 0
                    for i in range(left, right+1):
                        ans += nums_copy[i]
                    assert res == ans
                    
                    