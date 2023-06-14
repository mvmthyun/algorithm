# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
# a, b = map(int,input().split())
# a=int(input())
# b=int(input())

a = 1
b = 1
T = 5

T = int(input())
for i in range(1, T+1):
    a, b= map(int,input().split())
    print(f'Case #{i}: {a+b}')