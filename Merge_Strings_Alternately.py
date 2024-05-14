# Merge Strings Alternately Problem Number : 1768
def merge_alternate(word1, word2):
    res = ""
    i = 0
    while(i < len(word1) or i < len(word2)):
        if i < len(word1):
            res += word1[i]
        if i < len(word2):
            res +=word2[i]
        i = i+1

    return res

word1 = "abcd"
word2 = "pq"
print(merge_alternate(word1, word2))