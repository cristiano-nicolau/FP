def reverseDigits(value):
   return reverseAux(value, 0)

def reverseAux(partValue, partReversed):
   partReversed=""
   partValue=str(partValue)
   while  partValue!= "":
      partReversed=partReversed+partValue[0]
      
   return partReversed

reverseDigits(1234)