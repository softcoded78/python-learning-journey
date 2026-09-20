name = 'Icel'

# Basic string methods
print(name.upper()) # ICEL
print(name.lower()) # icel
print(len(name)) # 4 

# Checking string
print(name.isalpha()) # True 
print(name.isdigit()) # False 

# Replace and slice
print(name.replace('Icel', 'Icel the Coder')) # Icel the Coder
print(name[0]) # I 
print(name[-1]) # l 


print(name[:2]) # Ic 
print(name[2:]) # el 
print(name[:3]) # Ice 
print(name[::-1]) # lecI 


print(f"Hi\n{name}") # Hi
                      Icel
print(f"Course:\tBSCS") # Course: BSCS

# F-string
course = "BSCS"
print(f"Hi, I'm {name} from {course}") 
# Hi, I'm Icel from BSCS