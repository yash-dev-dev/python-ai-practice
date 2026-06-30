class ZeroDivisionError(Exception):
    pass
def safe_divide(a,b):
    try:
        if b==0:
            raise ZeroDivisionError ("number cannot be divided by zero")
        if not isinstance(a, int) or not isinstance(b, int):    
            raise TypeError("inputed values are not numbers")
        print("values:",a/b)
    except Exception as e:
        print("errors:",e)

        
    finally:
        print("division attempted")

#safe_divide(2,1)
#safe_divide(2,0)
#safe_divide("two",2)