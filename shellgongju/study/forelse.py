
for num in range(10,21):  #to iterate between 10 to 20
   count=0
   for i in range(2,num): #to iterate on the factors of the number
      if num%i == 0:      #to determine the first factor
	 count+=1
         j=num/i          #to calculate the second factor
         print '%d equals %d * %d' % (num,i,j)
         if i == num/2 :
		print 'count is %d' %(count)
         	break #to move to the next number, the #first FOR
   else:                  # else part of the loop
      print num, 'is a prime number'
