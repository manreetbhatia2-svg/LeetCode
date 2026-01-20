# input the roman number 
t = input("Enter a roman number ").upper()
s = list(t)

# Defining integer values for roman numbers
roman = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
for i in range (len(s)):
  s[i] = roman[s[i]]

# Converting roman to integer using addition and subtraction
i = 0
Int  = 0
while 0<= i < len(s):
  if i == len(s) -1:
    if s[i] <= s[i-1]:
      Int += s[i]
      i += 1
  elif s[i] >= s[i+1]:
    Int += s[i]
    i += 1
  else:
    Int += s[i+1] - s[i]
    i += 2

print (Int)