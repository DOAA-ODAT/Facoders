s1= ['Ahmad', 18, 17, 19.5, 8, 25]
s2= ['Sami', 20, 20, 19, 9, 28]
s3= ['Faris', 14.5, 16, 13, 7, 23]
i=1
while i ==1:
    name = input ("Enter student's name :")
    if name =='Ahmad':
            s1.remove('Ahmad')
            sum1 =sum(s1)
            print(name ,sum1)
    elif  name =='Sami':
                s2.remove('Sami')
                sum2 =sum(s2)
                print(name ,sum2)
    elif name =='Faris':
                s3.remove('Faris')
                sum3 =sum(s3)
                print(name ,sum3)
    else:
        print ("Student is not recorded  0")
