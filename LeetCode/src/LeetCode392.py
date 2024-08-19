class Solution(object):
    def isSubsequence(self, s, t):
        # 2 pointers one i is for the s string and j is for the t string
        i = 0
        j = 0

        # while loop keeps going if i and j pointers are not bigger than their strings s and t
        while i < len(s) and j< len(t):
            # here s at pointer i is equal to t at pointer j so the first letter in s was found in t
            # we can move to the next letters to make sure s is in j by moving both pointers
            if s[i]==t[j]:
                i+=1
                j+=1
            # here s at pointer i is not in t at pointer j so we move j and check if that letter
            # is in s at pointer i
            elif s[i] != t[j]:
                j+=1
        # we check if i is the length of s which means it made it all the way to the end and found 
        # all of its letters in t so we return true and if that is not the case we return false
        if i== len(s):
            return True
        else:
             return False
