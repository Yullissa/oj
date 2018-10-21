# class Solution:
def subarrayBitwiseORs(A):
    """
    :param A: List[int]
    :return: int
    """
    res = set()
    pre = set()
    for n in A:
        cur = set([n])
        for p in pre:
            cur.add(p|n)
        pre = cur
        for p in pre:
            res.add(p)
    return len(res)
    # res, cur = set(), set()
    # for i in A:
    #     cur = {i | j for j in cur} | {i}
    #     res |= cur
    # return len(res)

if __name__ == '__main__':
    A = [1,2,4]
    subarrayBitwiseORs(A)

