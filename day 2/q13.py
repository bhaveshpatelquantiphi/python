import re
p = raw_input()
x = True
while x:  
    if not re.search("[aeiou]",p[0]):
        break
    elif not re.search("[AEIOU]",p[0]):
        break
    else:
        print(p[0]+" is a Vowel")
        x=False
        break

if x:
    print(p[0]+" is a consonant")