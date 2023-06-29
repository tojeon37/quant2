# class XingAPI():
#     stock_name = "삼성"

# # result = XingAPI.stock_name
# # print(result)
# #클래스 밑에 변수 만들면 변수를 가져올수 있다.
# mXingAPI = XingAPI()
# result = mXingAPI.stock_name
# print(result)

# class XingAPI():
#     stock_name = "삼성"

#     def buy_calcul():
#         print("매수계산함수다")

# result = XingAPI.buy_calcul()
# print(result)

#클래스 안에 함수를 쓸때는 함수괄호에 (self)를 써주어야 한다.

# class XingAPI():
#     stock_name = "삼성"

# def __init__(self): 
#     #이줄은 함수에서 무조건 실행한다.
#     print("클래스 초기화") 
#     #변수를 정할때 초기값을 미리 정해주는 용도
#     print(dir(self))
    
#     stock_price = None
#     stock_drate = None

# result = XingAPI()
# print(result)




#self는 class내의 변수들을 다른 함수들이 변수를 잘 가져다 쓰도록 역할을한다.

# class XingAPI():
#     stock_name = "삼성"
    
#     def buy_func(self):
#         print("buy_fnc실행")
#         print(dir(self))

# result = XingAPI()

class XASession:
    def ONLogin(self):
        print("로그인 요청에 대한 수신")


class Main():
    def __init__(self) :
        print("메인 클래스다. 증권프로그램의 초기셋팅을 해놓는 곳이다.")
        
        print("로그인요청을 할거다")
        print("XASession 클래스에서 로그인 결과를 수신할거다")
        xa = XASession
        xa.ONLogin(self)
        
if __name__ == "__main__" :
    Main()
    