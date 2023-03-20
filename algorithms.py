# Programmer: 	Raza Bhatti
# Company:	Softgalaxy Technologies Inc.
# Website:	https://www.linkedin.com/in/softgalaxy
#
# Python 3.x Program Function: 
# 1. Take two parameters x,y and if x>y, recursively do following operation.
#     - Perform x=x-y operation, till x<y
# 2. Calcuate factorial of x.

import sys	#An include library to pass command line arguments to this program.
name_of_python_script = sys.argv[0]

#print(len(sys.argv))

#####################
# Program Functions #
#####################
#Function to check command line parameters and exit if missing expectations.
def fn_WrongNoOfParameters():
  print("")
  print("")
  print("\r\rKindly input parameter values for fn_Sub(x,y) and fn_Factorial(x) as shown below,")
  print("")
  print("python script_name.py 2,3 5")
  print("")
  print("")  
  exit()

def pm_Functions(x,y):
  # Sub functions sub(x,y)
  def fn_Sub(x,y):
    global recursion_Count  
    recursion_Count+=1
    x=x-y
    #print(x)
    if (x>y & recursion_Count<500): 
      fn_Sub(x,y)
    else:
      print("recursion_Count=",recursion_Count)

  # fn_Sub(x,y) function main body.
  if(x>y):
    print("Since x>y, calling fn_Sub(",x,y,")")  
    fn_Sub(x,y)
  else:
    print("Since x<y, so not calling fn_Sub(",x,y,"):")
  
# Sub functions factorial(x)
def fn_Factorial(x):
  global recursion_Count,  factorial_Result
  recursion_Count+=1
  factorial_Result*=x
  #print(factorial_Result)
  if(x>2 & recursion_Count<500):
     #print(x)
     fn_Factorial(x-1)    
  elif(x==0):
    print("recursion_Count=1, x!=1")     
  elif(x<0):
    print("Kindly give a value >=0 , Thanks.")     
  else:
    print("recursion_Count=",recursion_Count,", x!=",factorial_Result)

##Check if parameters are passed as expected, else prompt the user and exit. 
if(len(sys.argv)<3):
  fn_WrongNoOfParameters()
  
#Check if first function parameters are comma separated and atleast two values are passed as expected, else prompt the user and exit.
#Split arg2=values_for_fn_Sub for fn_Sub(x,y)
value_for_fn_Sub = sys.argv[1]
split_String=value_for_fn_Sub.split(",")

#print(split_String[0])

if(len(value_for_fn_Sub) < 2):
  fn_WrongNoOfParameters()  

x=split_String[0]
y=split_String[1]

  
#print(x,y)

values_for_fn_Factorial = sys.argv[2]
#print("x",int(len(value_for_fn_Sub)))
#print("y",int(len(values_for_fn_Factorial)))

#It all goes well with parameters, continue with the normal execution of the program.
print("\n============================================================================================================================")
print("\t\tThanks for inputting parameters as expected")
print("name_of_python_script: ",name_of_python_script,"\tvaluea for fn_Sub(",value_for_fn_Sub,"):","\tvalue for fn_Factorial(",values_for_fn_Factorial,"):")
print("\n============================================================================================================================")


#################################
## Start of programs main body ##
################################# 
recursion_Count=0  

factorial_Result=1
#factorial_Result="{:e}".format(1)

print("\n============================================================================================================================")
print("Calling pm_Functions(",x,y,")")  
pm_Functions(int(x),int(y))
print("\n============================================================================================================================")

print("\n============================================================================================================================")
recursion_Count=0
print("Calling fn_Factorial(",values_for_fn_Factorial,")")  
fn_Factorial(int(values_for_fn_Factorial))
print("\n============================================================================================================================")
 
