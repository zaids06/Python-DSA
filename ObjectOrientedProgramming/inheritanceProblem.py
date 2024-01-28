class India():
    def capital(self):
       print('New Delhi is the capital of India')
    def language (self):
        print('Hindi is the most widely spoken language of India.')
class USA():
    def capital(self):
        print( "Washington, D.C. is the capital of USA")
    def language(self):
        print("English is the primary language of USA.")
n=int(input())
if (n==1):
    India().capital()
    India().language()
elif(n==2):
    USA().capital()
    USA().language()
else:
    print('Invalid input. Please enter 1 for India or 2 for USA.')