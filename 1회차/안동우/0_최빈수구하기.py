import sys

sys.stdin = open("_최빈수구하기.txt")
#학생1000명
#제약 0이상 100이하
#최빈수 가장많이중복 높은 점수가 최빈수?
#점수는 문자열  
#중복 카운트 그중 최대 큰 수 출력
# print(f"#{} {}".format(,))
T=int(input())
T_num=int(input())
a=list(int,input().split())
b=set(a)

for z in T_num:#테스트 번호
    for i in a:
      print(b)