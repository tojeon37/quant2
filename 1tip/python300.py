# #11
# 삼성전자 = 50000
# 주식수 = 10
# 총평가금액 = 삼성전자 * 주식수
# print(총평가금액)

#12 변수 사용하기
# 시가총액 = 298000000000000
# 현재가 = 50000
# per = 15.79
# print(시가총액, type(시가총액))
# print(현재가, type(현재가))
# print(per, type(per))

#13 문자열 출력
# s = "hello"
# t = "python"

# print(s,"!", t)
# print(s+"!", t)

#14 값 계산
#15 type함수
# a = 123
# b = "123"
# print(a, type(a))
# print(b, type(b))

#16 문자열을 정수로 변환
# num_str = "720"
# num_int = int(num_str)
# print(num_int+1,type(num_int))


# #18 문자열을 실수로 변환
# num_str = "15.88"
# num_float= float(num_str)
# print(num_float, type(num_float))

# # 19문자열을 정수로 변환
# year = "2023"
# int = int(year)
# print(int, type(int))
# print(int+1, type(int))
# print(int+2, type(int))
# print(int+3, type(int))

#20 문자열을 정수로 변환
# a = 48584
# b = 36
# print(a*b)

#21 문자열 인덱싱
# letters = 'python'
# print(letters[:3])
# print(letters[0:2])
# print(letters[0],letters[2])

#22 문자열 슬라이싱
#음수는 문자열의 뒤에서부터 인덱싱, 시작인덱스생략은 0, 끝 생략하면 문자열의 끝 
# license = "72조3565"
# print(license[3:])
# print(license[-4:])
# print(license[:2])
# print(license[2:])
# print(license[3:])
# print(license[-4:])

# #23 문자열 인덱싱 !
# string= "홀짝홀짝홀짝"
# print(string[0],string[2],string[3])
# print(string[::2])

# #24 문자열 거꾸로 슬라이싱  !
# string = "python"
# print(string[::-1])
# print(string[::-2])
# print(string[1::])
# print(string[2::])
# print(string[::2])

# #25 문자열 치환
# phone="010-1234-5678"
# phone2 = phone.replace("-"," ")
# print(phone2)

# #26 문자열 다루기
# phone="010-1234-5678"
# phone2 = phone.replace("-","")
# print(phone2)

#27 문자열 다루기 2
# url = "http://naver.com"
# print(url[:3])
# print(url[3:])
# print(url[-3:])
# print(url[:-3])
# url1 = url.split(".")
# print(url1[0])
# print(url1[1])
# print(url1[-1])
# print(url1[-2])


#28 문자열은 변경불가
# lang = 'python'
# lang[0] = 'P'
# print(lang)

# #29 replace 메서드
# string = "abcadeafgh12345"
# string = string.replace('a', 'A')
# string = string.replace('b', 'B')
# print(string)

# #30 replace메서드 그냥 변경은 안되고 새로운 변수에 넣어줘야한다.
# string = 'abcd'
# string.replace('b', 'B')
# print(string)


# #31 문자열 합치기
# a = '3'
# b = '4'
# print(a+b)

# #32 문자열 곱하기
# print("Hi"*3)


# #33 문자열 곱하기
# print("-"*80)

#34 문자열 곱하기
# t1 = 'python'
# t2 = 'java'
# print((t1+t2)*4)


#35 문자열 출력
# name1 = "전태옥"
# age1 = 10
# name2 = "안현진"
# age2 = 20
# print("이름: %s 나이: %d" % (name1,age1))
# print("이름: %s 나이: %d" % (name2,age2))


#36 문자열 출력 format
# name1 = "전태옥"
# age1 = 35
# name2 = "안현진"
# age2 = 32
# print("이름: {} 나이: {}".format(name1,age1))
# print("이름: {} 나이: {}".format(name2,age2))


#37 문자열 출력 f-string
# name1 = "김민수" 
# age1 = 10
# name2 = "이철희"
# age2 = 13
# print(f"이름: {name1} 나이: {age1}")
# print(f"이름: {name2} 나이: {age2}")

#038 컴마 제거하기
# 삼성전자의 상장주식수가 다음과 같습니다. 
# 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"
# 컴마제거 = 상장주식수.replace(",","")
# 타입변환 = int(컴마제거)
# print(타입변환,type(타입변환))

# 039 문자열 슬라이싱
# 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])
# 숫자 = "123456789"
# print(숫자[:4])

# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.

# data = "   삼성전자    "
# data1 = data.replace(" ", "")
# print(data1)
# data2 = data.strip()
# print(data2)

# rstrip 메서드
# 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.

# data = "     039490"
# data=data.rstrip()
# print(data)


# 040 strip 메서드
# 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.

# data = "   삼성전자    "
# data1 = data.replace(" ", "")
# print(data1)
# data2 = data.strip()
# print(data2)


# 041 upper 메서드
# 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.

# ticker = "btc_krw"
# a = ticker.upper()
# print(a)

# 042 lower 메서드
# 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.

# ticker = "BTC_KRW"
# b = ticker.lower()
# print(b)

#043 capitalize 메서드 : 앞에를 대문자로 변경
# 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.

# a = 'hello'
# b = a.upper()
# print(b)
# a = a.capitalize()
# print(a)

#044 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.

# file_name = "보고서.xlsx"
# print(file_name.endswith("xlsx"))

# 045 endswith 메서드
# 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.

# file_name = "보고서.xlsx"
# print(file_name)
# file_name = file_name.endswith("xlsx","xls")
# print(file_name)
