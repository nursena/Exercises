def geometry(shape):
    if len(shape)==3:
        a=shape[0]
        b=shape[1]
        c=shape[2]

        if (a+b)>c and (a+c)>b and (b+c)>a :
            if (a==b) and (a==c) and (b==c):
                print("equilateral triangle")
            if (a==b) and (a==c):
                print("isosceles triangle")
            else:
                print("scalene triangle")

    elif len(shape)==4:
        a=shape[0]
        b=shape[1]
        c=shape[2]
        d=shape[3]
        if (a==b) and (a==c) and (a==d):
            print("square")
        elif (a==c) and (b==d):
            print("rectangle")
        else:
            print("scalene quadrilateral")

    else:
        print("can not know what it is")

while(True):
    number_of_edges=input("enter the number of edges or if you want to end, please press w : ")
    if number_of_edges=="w":
        break

    number_of_edges=int(number_of_edges)

    if (number_of_edges == 3):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        geometry([a,b,c])

    elif (number_of_edges == 4):
        a=int(input("a:"))
        b=int(input("b:"))
        c=int(input("c:"))
        d=int(input("d:"))
        geometry([a,b,c,d])

    else:
        print("please,try again")
