str1 = (input("Enter your first word or phrase"))
str2 = (input("Enter your second word or phrase"))

str1_Lower = str1.lower()
str2_Lower = str2.lower()

for a in [' ','`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','[','}',']','{','|','\\',"",'',';',':',',','<','.','>','/','?','1','2','3','4','5','6','7','8','9','0']:
    if a in str1_Lower:
        str1_Lower = str1_Lower.replace(a,"")

for a in [' ','`','~','!','@','#','$','%','^','&','*','(',')','_','-','=','+','[','}',']','{','|','\\',"",'',';',':',',','<','.','>','/','?','1','2','3','4','5','6','7','8','9','0']:
    if a in str2_Lower:
        str2_Lower = str2_Lower.replace(a,"")
        
if(sorted(str1_Lower)==sorted(str2_Lower)):
    print("These two phrases are anagrams.")
else:
    print("These two phrases are not anagrams.")

 
    








