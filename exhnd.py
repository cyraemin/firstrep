#there are a few errors through which the program flow can get disrupted.
#but we can handle these through certain keywords, this is called exception handling.
#try- wraps the block of code that might cause exception
#except- handles exception if it occurs
#else-runs code only if no exception
#finally- runs code no matter what
#raise- manually throw an exception--(this stops the execution of program, so use try and except along with it)
a=int(input("enter your age- "))
try:
    if a<10 or a>18:
        raise ValueError("your age must be between 10 and 18")
except Exception as err:
    print(f"exception as {err}")
else:
     print("no exception occured")
finally:
     print("runs code no matter what")
print("done")