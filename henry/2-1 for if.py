# x=0

# if x>0 :
#     print("값이 0보다 큽니다")
    
# elif x<0: 
#     print("값이 0보다 작습니다")
    
    
# else :
#     print("값은 0 입니다")
    

# num=1

# while num<5:
#     print(num)
#     num = num+1
    
    
# num=2

# while num<10:
#     if num%2 ==0 : #짝수이면
#         print(f'{num}은 짝수입니다.')
#     num = num+1

    
    
# money = 1000

# while True:
#     money = money-100
#     print(f'잔액은{money}입니다')
    
#     if money <=0:
#         break


# var = [1,2,3]

# for i in var:
#     print(i)
    
# var = [10,15,17,20]
# for i in var:
#     if i%2 ==0:
#         print(f'{i}는 짝수입니다')
#     else:
#         print(f"{i}는 홀수입니다")


# range 함수
# for i in range(10):
#     print(i)

# a리스트의 제곱을 구하려면
# 일반적 형태
# a = [1,2,3,4,5,6,7,8,9]

# result = []
# for i in a:
#     result.append(i**2)

# print(result)

# 리스트 내포형태
# a = [1,2,3,4,5,6,7,8,9]

# result = [i**2 for i in a]
# print(result)

# for문 출력시 오류발생되면 처음부터 다시해야됨,
# for문 예외처리를 할때 쓰임
# try:   #일단 먼가해라
#     expr
# except:  #하다가 오류나면 출력하고 다음루프로 넘어가라
#     error-handler-code
# num = [1,2,3,"4",5]
# for i in num:
#     print(i**2)
# 4에서 오류가 나서 5가 실행이안됨
# num = [1,2,3,"4",5]
# for i in num:
#     try:
#         print(i**2)
#     except:
#         print('Error at:' +i)
