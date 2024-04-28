"""
코드 작성 일자 : 2024-04-24
코드 작성자 : 전석우
코드 이름 : utils.py
코드 목록 : 유용한 함수를 따로 저장하여 두고 나중에 불러와 사용하기 위함
"""


def factorial(x):
    if x <= 1:
        return 1
    return x * factorial(x - 1)

def gugudan(x):
    for i in range(9):
        print((i+1) * x)
