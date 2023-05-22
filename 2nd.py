''' Program to reverse string using slice operator '''

def reverse(str):   
    str = str[::-1]   
    return str   
    
# s = "Omar"  
# s = char(input('Enter a character')) --> for taking character as a input, no need to specify char...
s =input('Enter a character')
print ("The original string  is : ",s)   
print ("The reversed string using extended slice operator  is : ",reverse(s))