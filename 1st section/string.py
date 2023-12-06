def lastwordlen(sentence):
    sentence=sentence.strip()
    #strip method removes leading and trailing whitespaces in the sentence 
    
    words=sentence.split()
    #split method helps to split the sentence into words
    return len(words[-1])
   #returns the length of the last word

sentence =input("enter the sentence")
#input sentence from the user
ans=lastwordlen(sentence)
#storing the result of lastwordlen function 
print(ans)