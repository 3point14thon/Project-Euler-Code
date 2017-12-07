#Takes user input and finds the largest prime factor
def main():
  number1 = int(raw_input('Input number to find its greatest prime factor: '))
  number2 = factor(number1)
  while number1 != number2:#checks to make sure number can't be reduced more
    number1 = number2
    number2 = factor(number2)
  print(number2)#once the number can't be reduced any more the value is the greatest prime factor

def factor(num): # returns the largest factor of the input number
  n = 2
  while num%n != 0 and num > n: n +=1
  if num == n: 
    return num
  return num/n
main()
