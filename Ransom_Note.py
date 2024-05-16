# Ransom Note problem Number : 383
def rm(ransomNote, Magazine):
    for i in range(0,len(ransomNote)):
        if ransomNote[i] != magazine[i]:
            return False
                
    return True

       
        
            
                
ransomNote = "aa"
magazine = "aab"          
print(rm(ransomNote,magazine)) 


# str = "acbd"
# print(str[3])