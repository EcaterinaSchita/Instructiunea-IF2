x=int(input('locul lui ionel este'))
if(x%4==1) and (x<1000):
    print('tricou alb')
elif (x%4==2) and (x<1000) :
    print('tricou rosu')
elif (x%4==3) and (x<1000) :
    print('tricou albastru')  
elif (x%4==0) and (x<1000):
    print('tricou negru ')
else:
    print('eror')    