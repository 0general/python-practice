#2보다 큰 자연수 N을 입력으로 받아 2부터 N까지의 자연수 중에서 완전수를 출력하는 프로그램

def PerfectNum(n):
    s=0; i=1
    while s <= n and i <= int(n / 2):
        if n % i == 0:
            s += i; i += 1
        else:
            i += 1
    if s == n: print(n, end=' ')

while True:
    n = float(input("2보다 큰 자연수 N을 입력하시오 : "))
    if n > 0 and n % 1 == 0: break
    else: print("잘못된 입력입니다. 다시 입력하세요")

s = 0 #약수의 합
i = 1
while s <= n and i <= int(n/2):
    if n%i==0: s += i; i += 1
    else: i+=1

if s == n: print("N은 완전수입니다.")
else: print("N은 완전수가 아닙니다.")

# 알고리즘을 확인하기 위해 완전수를 제대로 찾는지 확인
print("======================================")
r = int(input("\n\n반복횟수 R을 입력하세요 : "))
for i in range(2,r+1):
    PerfectNum(i)