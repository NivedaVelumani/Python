weight=int(input('weight'))
unit=input('(L)bs or (K)g:')
if unit.upper()=='L':
    convert=weight*0.45
    print("you are ",convert ,"kilos")
else:
    convert= weight/0.45
    print("you are",convert ,"lbs")
