TC = int(input())

for t in range(TC):
    N = int(input())
    cnt = [1 for _ in range(10)]        # cnt[i]는 전체 n자리 수에서 가장 왼쪽에 해당 숫자 i가 몇 개 있는지를 의미
                                        # n = 1인 n자리수는 0 ~ 9로 각 숫자 i가 1개씩이다
                                        # 0 앞에는 0만 올 수 있으며, 9 앞에는 0~9 모두 올 수 있다
                                        # 현재 n자리 수에서 cnt[0]이 2라면, 다음 n자리수에서 가장
    for i in range(1,N):
        for j in range(10):
            for k in range(j):
                cnt[k] += cnt[j]


    print(sum(cnt))