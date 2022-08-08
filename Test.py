print("hello wolrd")
def 함수(a,b) :
    print(a + b)
함수(5,6)



def print_with_smile(str):
    print(str, " xD")
print_with_smile('배고파')


def sum (a, b):
    print(a+b)
sum(5,7)


def print_coin():
    print("비트코인")
print_coin()

for i in range(5):
    print_coin()


for i in range(10):
    print("무엇이든 나와라")


for b in range(3):
    print("오늘은 과연")

a = [1,2,3,4,5,1,4]
print(a.index(4))

print(str(a))




list1 = list(range(20))
# new_list가 5, 8, 11, 14의 값을 가지도록 list1을 slice하세요
new_list = list1[5:15:3]

print(new_list)


# reverse_list가 17, 13, 9, 5의 값을 가지도록 list1을 slice하세요
reverse_list = list1[17:4:-4]

print(reverse_list)


list1 = list(range(20))
print(list1)