import time

N = int(input('2 이상의 자연수 입력 : '))
while N <= 1:
    print(N, '은(는) 2 이상의 자연수가 아닙니다.')
    N = int(input('2 이상의 자연수 입력 : '))
starttime = time.time()
a = list(range(N+1))
a[1] = 0
i = 2
while i<= N/2:
    j = 2
    while i*j <= N:
        a[i*j] = 0
        j += 1
    i += 1
for i in range(1, N+1):
    if a[i]: print(a[i])
endtime = time.time()

print('걸린 시간은 : ' ,(endtime-starttime))
