"""
倍增
用于处理图的问题, 一个节点只会指向唯一的一个节点
然后求从一个节点移动k步后会到达的节点, 或者路径上的节点和(一般k会比较大)

算法的思想是处理一个节点移动2^i步后会到达的节点/路径上的节点和, 然后将k转化为2的幂相加
"""

"""
! 求移动k步所到达的节点
"""

def binary_lifting(nxt, k):
    """倍增

    Args:
        nxt ([int]): nxt[i]记录节点i的下一个节点
        k (int): 走k步

    Returns:
        pa: pa[i][j]表示i走2^j步所到的节点
    """
    n = len(nxt)
    m = k.bit_length()-1
    pa = [[p] + [None]*m for p in nxt]  #* n*(m+1)的矩阵pa， pa[i][j]表示i走2^j步所到的节点
    for i in range(m):
        for x in range(n):
            p = pa[x][i]    #* x走2^i步到达p
            pp = pa[p][i]   #* p走2^i步到达pp
            pa[x][i+1] = pp #* x走2^(i+1)步到达pp
    return pa


"""
! 求移动k步所到达的节点, 以及路径上的所有节点的和
"""

def binary_lifting(nxt, k):
    """倍增

    Args:
        nxt ([int]): nxt[i]记录节点i的下一个节点
        k (int): 走k步

    Returns:
        pa: pa[i][j]表示i走2^j步所到的节点
    """
    n = len(nxt)
    m = k.bit_length()-1
    pa = [[(p, p)] + [None]*m for p in nxt]  #* n*(m+1)的矩阵pa， pa[i][j]表示i走2^j步所到的节点
    for i in range(m):
        for x in range(n):
            p, s= pa[x][i]    #* x走2^i步到达p, 路径上的和为s
            pp, ss = pa[p][i]   #* p走2^i步到达pp, 路径上的和为ss
            pa[x][i+1] = (pp, s+ss) #* x走2^(i+1)步到达pp, 路径上的和为s+ss
    return pa
    