# 设计一个判断给定的大于1的正整数是不是质数的函数。质数是只能被1和自身整除的正整数（大于1)，如果一个大于 1的正整数 N 是质数，那就意味着在 2 到 N - 1 之间都没有它的因子。



def judge_prime(n:int) -> bool:
    flag = True
    if n <= 1:
        return flag
    for index in range(2, n -1):
        if n % index == 0:
            flag = False
    return flag

print(judge_prime(3))




