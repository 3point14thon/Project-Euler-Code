#Gives the largest palandrom that can be created by multiplying two three digit integers
def main():
  #set as the two largest three digit numbers
  i = 999
  answer = 9
  #checks through three digit integers 
  while i != 0:
    j = 999
    pal = list(str(i*j)) 
    while checkpal(pal) and j != 0:
      j -= 1
      pal = list(str(i*j))
    if answer < int(''.join(pal)):#if the product of i and j is a pallandrom and larger than the previous pallandrom found it replaces it as 'answer'
      answer = int(''.join(pal))
    i -= 1
  print(answer)

#checks if the input number is a pallandrom by converting it to a list spliting the list in half and checking if the first half is the same as the reverse of the second half
def checkpal(num): 
  return(num[:len(num)//2] != num[:-len(num)//2-1:-1])
main()
