def symmetric(m_set,n_set):
    res = m_set.symmetric_difference(n_set)
    resF = sorted(res)
    for result in resF:
        print(result)
if __name__=="__main__":
    m = int(input())
    m_set = set(map(int,input().split()))
    n = int(input())
    n_set = set(map(int,input().split()))
    symmetric(m_set,n_set)