def endX(s):
   c=0
   n=""
   for l in s:
      if l=='x':
         c+=1
      else:
         n+=l
   n=n+c*"x"
   return (n)

def main():
    print(endX("xxcsv"))
    print(endX("dsxr"))
    print(endX("xaxcxsxv"))

main()