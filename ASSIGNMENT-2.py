# 1 Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples


my_tuple = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

def sort_tuple(my_tup):

   my_len = len(my_tup)
   for i in range(0, my_len):

      for j in range(0, my_len-i-1):
         if (my_tup[j][-1] > my_tup[j + 1][-1]):
            temp = my_tup[j]
            my_tup[j]= my_tup[j + 1]
            my_tup[j + 1]= temp
   return my_tup


print("The tuple is :")
print(my_tuple)

print("The sorted list of tuples are : ")
print(sort_tuple(my_tuple))




# 2 Write a Python program to print a dictionary whose keys should be the alphabet from a-z and the value should be corresponding ASCII values

my_dict = {}
for i in range(97, 97 + 26):
    
    my_dict[chr(i)] = i
print(my_dict)























