# Ransom Note problem Number : 383
def rm(ransomNote, Magazine):
    for char in set(ransomNote):
        if ransomNote.count(char) > magazine.count(char):
            return False
    return True

       
        
            
                
ransomNote = "aab"
magazine = "baa"          
print(rm(ransomNote,magazine)) 


# str = "acbd"
# print(str[3])