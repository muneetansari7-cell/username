
import random as rd
nonchar = "+=)(*&^%$#@!)"
nonchar2="-._"
while True:
    
    imp = input("enter your username: ")
    lens = int(input("enter the lenght of your numbr(limit till 4 digit only)"))
    
    total=len(imp)+lens-8
    # Check username length BEFORE breaking
    if len(imp)+lens<8:
        otp=f"character should be more then 8 chracters \n (your currently {total} charcters short)"
        if "-" in otp:
            print(otp.replace("-",""))
        continue
    elif len(imp)>=30-lens:
        print(f"characters should be less then {30-lens} ")
        continue

    # Check characters BEFORE breaking
    if any(char in imp for char in nonchar) and any(char in imp for char in nonchar2):
        print("there is an error you have mixed valid with invalid chractaer ")
        continue
    elif any(char in imp for char in nonchar):
        print("invalid charcter detcted")
        continue
    elif any(char in imp for char in nonchar2):
        print("perfect")
        continue
    
    # Now check lens and generate number
    if lens==1:
        rnd = rd.randint(1,9)
        break
    elif lens==2:
        rnd = rd.randint(10,99)
        break
    elif lens==3:
        rnd = rd.randint(100,999)
        break
    elif lens==4:
        rnd = rd.randint(1000,9999)
        break
    else:
        print("the limit should be between 1-4 not more than that")
    
vari = f"{imp}" + f"{rnd}"
print(vari)
