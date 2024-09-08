print("Hello World")
#
def input_value():
    a = input("Nhap mot so:")
    print(a)

b = input_value()

def check_even_or_odd(a:int):
    if a%2 == 0:
        b = True
        print(f'{a} chia het cho 2')
    else:
        b = False
        print(f'{a} khong chia het cho 2')
    return b

b = check_even_or_odd(7)

def check_so_nguyen_to(a:int):
    b = a+1
    is_nguyen_to = True
    for i in range(2, b):
        if a%i == 0 and a != i:
            is_nguyen_to = False
            break

    if is_nguyen_to:
        print(f'{a} la so nguyen to')
    else:
        print(f'{a} kh la so nguyen to')
    return is_nguyen_to

a = check_so_nguyen_to(13)

def print_so_nguyen_to_tu_1_den_100():
    for a in range(1,101):
        b = check_so_nguyen_to(a)
        if b:
            print(a)

c = print_so_nguyen_to_tu_1_den_100()

def print_so_chan_tu_1_den_100():
    for a in range(1,101):
        b = check_even_or_odd(a)
        if b:
            print(a)

c = print_so_chan_tu_1_den_100()

def tim_so_chan_dau_tien(a: list):
    for i in a:
        if i%2==0:
            print(i)
            break

b = [1,2,6,2,4]
a = tim_so_chan_dau_tien(b)




