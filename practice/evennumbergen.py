
def even_numbers(limit):
    for num in range(0,limit):
     if num%2==0:
        yield num
limit=int(input("enter the limit of the number"))
stall=even_numbers(limit)
for value in stall:
   print(value) 
    