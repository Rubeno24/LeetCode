# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        #use binary search to see what number a user picks from 1 to n
        # we start at 1 and go to n which will be the number the users picks. So it could be 1 to 10 where 10 is n
        start = 1
        end = n 
        # we want to keep going until start is less then and equal to end. Once start is bigger it means the 
        # number was not found and we return -1
        while(start<=end):
            # we define the middle number in the while loop since its gonna be adjusted everytime untill we find the number
            middle = (start+end)//2
            # We pass in middle to the api and if it returns 0 the number was found and we return0
            if guess(middle) == 0:
                return middle
            # We pass in middle to the api and if it returns -1 the number they guessed is higher then the middle 
            # number so we get rid of all the bigger numbers
            elif guess(middle) == -1:
               end=middle-1
            # We pass in middle to the api and if it returns 1 the number they guessed is lower so we get rid of the smaller number
            elif guess(middle) ==1:
              start=middle+1
        return -1