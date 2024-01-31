TC = int(input())

for t in range(TC):
    N = int(input())
    cnt = [1 for _ in range(10)]        # cnt[j]는 전체 n자리 수에서 가장 왼쪽에 해당 숫자 j가 몇 개 있는지를 의미
                                        # n = 1인 n자리수는 0 ~ 9로 각 숫자 j가 1개씩이다
                                        # 0 앞에는 0만 올 수 있으며, 9 앞에는 0~9 모두 올 수 있다
                                        # cnt[0]부터 cnt[j]에 현재 cnt[j] 값을 더해주면
                                        # cnt[j]로 인해서 그 앞에 오는 숫자의 개수를 구할 수 있다
                                        # 이 단계를 0부터 9까지 n번 반복하면, n자리 수에서 가장 앞의 있는 수의 개수들을 구할 수 있으며
                                        # 이게 곧 n자리 수의 개수가 된다
    for i in range(1,N):
        for j in range(10):
            for k in range(j):
                cnt[k] += cnt[j]


    print(sum(cnt))