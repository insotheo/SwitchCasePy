import SWITCH_CASE_MODULE as sc #You have to import it!!!!

print("Hello! There are some examples!\n")

def example_1():
     import random as rnd
     a : int = rnd.randint(1, 6)

     def defaultWrite():
          print("I don't even know the value of a")
          print("-" * 15)
          print(f"a = {a}")

     sc.SWITCH(a, 
               sc.CASE(1, lambda: print("a = 1")),
               sc.CASE(2, lambda: print("a = 2")),
               sc.CASE(3, lambda: print("a = 3")),
               sc.CASE(4, lambda: print("a = 4")),
               sc.CASE(5, lambda: print("a = 5")),
               default_action = defaultWrite)
     
def example_2():
     pi : float = 3.1415

     sc.SWITCH(pi,
               sc.CASE(float(4), lambda: print("Too big! It can't be true")),
               sc.CASE(pi, lambda: print("A MAGICIAN!!!"), False),
               sc.CASE(pi, lambda: print("You did it again..."), False),
               sc.CASE(pi, lambda: print("And again..."), False),
               sc.CASE(pi, lambda: print("And one more time"), True), #If there is a true or nothing switch finishes checking cases for the same values
               sc.CASE(pi, lambda: print("And never more"))
               )
     
def example_3():
     one_type_data : str = "Switch-Case in Python"

     sc.SWITCH(5,
               sc.CASE(3, lambda: print("Hello, World!")),
               sc.CASE(21, lambda: print("5 != 21")),
               sc.CASE(one_type_data, lambda: print("How did you do it???"))
               )
     
#example_1()
#example_2()
#example_3()