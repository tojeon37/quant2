# print(__name__)


# class MyStock():
#     def 매수용조건문 ():
#         print("계산들")
#     def 매도용조건문 ():
#         print("계산들")
#     def 조건검색 ():
#         print("조건검색")

# class는 대그룹
# def 함수는 소그룹으로 이해.


# def 매수계산함수():
#     print("여기는 매수계산함수다")
# #출력이 안된다.함수는 메모리에 저장만 된 상태이다. 

# 매수계산함수()
# 매수계산함수()
# 매수계산함수


# def 매수계산함수(가격,수량):
#     결과 = 가격*수량
#     print("내가 매수하려는 총 금액 %s" %결과)
# 매수계산함수(3000,20)

#디버그창에서 arguments 는 변수를 뜻함

# def setData(price:int=3000, Quantity:int=None, stock_name:str=None): 
#     #setData는 내가 가지고 있는 데이터를 어딘가에 올려주겠다는 의미
#     print("가격: %s, 수량 : %s, 종목 : %s" %(price,Quantity,stock_name))

# setData(Quantity=5, stock_name="삼성")
#변수값을 처음에 모르면 초기값 None을 입력해도 된다.
#변수가 정수인지 문자인지 알기쉽게 변수명 옆에 :int 나 :str을 붙이면 나중에 보기 편하다.



def setData(price:int=3000, Quantity:int=None, stock_name:str=None): 
    result = price*Quantity
    # print("매수할 가격: %s, 종목이름 : %s" %(result,stock_name))

    return result
#return은 함수 밖으로 데이터를 빼준다. 따라서 리턴이 뜨면 함수가 끝을 맺고 다음 줄로 넘어간다. 리턴을 쓰면 메모리 밖으로 나갈수 있게 뚫려있는다.


total = setData(Quantity=5, stock_name="삼성")
#None은 int와 곱할수 없다.
print("총금액 : %s" %total)


#함수는 소그룹이다.