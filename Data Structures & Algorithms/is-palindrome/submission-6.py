class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr=[]
        for letter in s:
            if letter == " " or letter.isalnum() is False:
                continue
            arr.append(letter.lower())
        
        i, j = 0, len(arr)-1
        while i <= j :
            if arr[i] == arr[j]:
                i+=1
                j-=1
                continue
            else:
                return False
            
        return True