#Created by Insotheo(c) in 2024 on April 24

#Class for implementing "case" functionality
class CASE:
     val : any = None #This is the comparison value
     act : any = None #Action will be performed when the case is completed
     breakable : bool = True #Should do "break" when the case is completed. Default value is true

     def __init__(self, value, action, breakable = True) -> None:
          self.val = value
          self.act = action
          self.breakable = breakable

#Use this function to check if a variable(value: any) is null
def is_null(value : any) -> bool:
     if value == None:
          return True
     
     return False

#ABOUT def SWITCH-----
#object is the value to be compared to
#*cases is a list of CASE objects to perform actions if the value is correct
#default_action if a case where none of the cases were correct
#-----
def SWITCH(object: any, *cases: CASE, default_action = None) -> None:
     if is_null(object) or is_null(cases):
          return
     
     done_main_thread_of_cases : bool = False

     for case in cases:
          if type(object) != type(case.val):
               print("ERROR: Can't compare different data types!", end=" ")
               print(f"Exeption index is [{cases.index(case)}]")
               return

          if object == case.val:
               case.act()
               done_main_thread_of_cases = True

               if case.breakable:
                    break

               else:
                    continue


     if done_main_thread_of_cases == False:
          if is_null(default_action) == False:
               default_action()