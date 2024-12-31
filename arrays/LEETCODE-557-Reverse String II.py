## 557. Reverse Words in a String III
# Declare a string to concatenate the result
# Declare two pointers l and r to keep track of the start and end of a word
# Iterate through the string
# If the character at r is not a space, increment r
# If the character at r is a space, reverse the substring from l to r and concatenate it to the result
# Increment
# Return the result
# Time Complexity: O(n)


class Solution(object):
  def reverseStr(self, s, k):
    res = ''
    l, r = 0,0

    while r< len(s):
      if s[r] != ' ':
        r +=1
      else:
        res+= s[l:r+1][::-1]
        r+=1
        l = r
    res += ' '
    res += s[l:r+2][::-1]
    return res[1:]