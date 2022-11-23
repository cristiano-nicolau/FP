s=input("String= ")
s2=""
s3=""
def func(s,s2,s3):
    for i in range(len(s)):
        s2+=s[i]
        s3=s[i:]
        if s2 in s3:
            s4=s2
    return s4

print(func(s,s2,s3))