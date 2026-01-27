class subfieldsinAI():
    def subfields():
        print("Subfields in AI are:")
        print("Machine learning")
        print("Neural networks")
        print("vision")
        print("robotics")
        print("speech processing")
        print("Natural language processing")
    
    def oddeven():
        num=int(input("Enter the number:"))
        if(num%2==0):
            print(num,"is even number")
        else:
            print(num,"is odd number")
        return num

    def eligible1():
        gen=input("Your Gender:")
        age=int(input("Your age"))
        if(gen=="male" and age>=21):
            print("Eligible")
        elif(gen=="female" and age>=18):
            print("Eligible")
        else:    
            print("Not Eligible")
            return gen

    def percentage():
        sub1=int(input("SUBJECT1:"))
        sub2=int(input("SUBJECT2:"))
        sub3=int(input("SUBJECT3:"))
        sub4=int(input("SUBJECT4:"))
        sub5=int(input("SUBJECT5:"))
        tot=sub1+sub2+sub3+sub4+sub5
        print("total:",tot)
        per=float(tot/500*100)
        print("percentage:",per)
        return per
    def triangle():
        height=float(input("Height:"))
        brdth=float(input("Breadth:"))
        area=(height*brdth)/2
        print("Area of Triangle:",area)
        height1=float(input("Height1:"))
        height2=float(input("Height2:"))
        breadth=float(input("Breadth:"))
        peri=height1+height2+breadth
        print("Perimeter of Triangle:",peri)
        return peri
                        
