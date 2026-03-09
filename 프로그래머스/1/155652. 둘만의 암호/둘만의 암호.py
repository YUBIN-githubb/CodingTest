def solution(s, skip, index):
    answer = []
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(0,len(skip)):
        alphabet.remove(skip[i])  
    
    for i in range(0,len(s)):
        piece = []
        for j in range (1,index+1):
            piece.append(alphabet[(alphabet.index(s[i]) + j)%len(alphabet)])
        answer.append(piece[-1])
        
    return "".join(answer)
    
    
            
            
            
            
        
        
        
