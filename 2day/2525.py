# KOI 전자에서는 건강에 좋고 맛있는 훈제오리구이 요리를 간편하게 만드는 인공지능 오븐을 개발하려고 한다. 인공지능 오븐을 사용하는 방법은 적당한 양의 오리 훈제 재료를 인공지능 오븐에 넣으면 된다. 그러면 인공지능 오븐은 오븐구이가 끝나는 시간을 분 단위로 자동적으로 계산한다. 
# 또한, KOI 전자의 인공지능 오븐 앞면에는 사용자에게 훈제오리구이 요리가 끝나는 시각을 알려 주는 디지털 시계가 있다. 
# 훈제오리구이를 시작하는 시각과 오븐구이를 하는 데 필요한 시간이 분단위로 주어졌을 때, 오븐구이가 끝나는 시각을 계산하는 프로그램을 작성하시오.

# 첫째 줄에는 현재 시각이 나온다. 현재 시각은 시 A (0 ≤ A ≤ 23) 와 분 B (0 ≤ B ≤ 59)가 정수로 빈칸을 사이에 두고 순서대로 주어진다.
# 두 번째 줄에는 요리하는 데 필요한 시간 C (0 ≤ C ≤ 1,000)가 분 단위로 주어진다.

# A, B=map(int,input().split())
# C = int(input())

A = 14
B = 20

C = 30

minResult = 0
hourResult = 0

# if B + C > 60:
#     minResult = (B + C) / 60
#     hourResult = A + ((B+C) % 60)
# elif B + C < 60:
#     minResult = B + C
#     hourResult = A

if (B + C) / 60 > 0:
    minResult = (B + C) % 60
    hourResult = int(A + ((B+C) / 60))
    if hourResult >= 24:
        hourResult -= 24
else:
    minResult = B + C
    hourResult = A

print(A, "", B)
print(hourResult, minResult)