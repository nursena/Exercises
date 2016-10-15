while True:
    number=1
    n=input("enter your value(to exit press q)")
    if n=="q":
        break
    else:

        for a in range(2,int(n)+1):
            number*=a
        print(number)
