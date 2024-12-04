from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        read = 0 
        write = 0
        #keeps going until read is greater then the array lenght
        while read < len(chars):
            #gets current chacter
            currChar = chars[read]
            #assigns the count of that character
            count = 0

            #keeps going till end of array and keeps counting occurces of that character
            while read < len(chars) and currChar == chars[read]:
                #advances read and the count
                read += 1
                count += 1
            #breaks out of loop and write that character and moves over by
            chars[write] = currChar
            write+=1
            #if the count is greater than one also writes the count of the character
            if count > 1:
                for x in str(count):
                    chars[write] = x
                    write +=1 
        #returns the lenght of the list which is the second pointer write 
        return write

# Test the function
x = Solution()
chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]


print(chars[:x.compress(chars)])
