def factorial(n):

    if n == 0:
        return 1
        
    elif n <= 0:
          
          print("Too negative!")
    elif n >= 10:
          print("Too loud! Keep it down!")
    else:
        return n * factorial(n-1)
        
n=int(input("Input a number under eleven : "))
print("The factorial of", n, "is:", factorial(n))



def num():
    
      if num <= 10:
            return num 
      

num()

#def ask_again():
      #ans = str(input("Do you want to put another number in y/n?  "))
      
      #if ans == 'y':
            #return num

      #else:

            #quit
#ask_again()   
# ('y', 'n') 
      
            
      #else:
            #if ans == 'n':

                  #print ("Good bye!")
                  #quit

                
#while True:
      #result = -1
      #while (result < 0):
            #result = getNumber()
      #fact = factorial(result)
      #print("Factorial of ", result, "is", fact)