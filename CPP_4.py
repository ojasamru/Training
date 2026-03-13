 #for i in range(1,5):
 #   if i ==3:
#         continue
#     print(i)

#     pairs = [(1, 5), (2, 4), (4, 2), (5,1)]
#     for pair in pairs:
#         print(*pair)

# for i,j in zip(range(1,6), range(5,0,-1)):
#     if i==3 and j==3:
#         continue
#     print(i, j)

# i=1
# while i<=5:
#     print(i)
#     i=i+1

# username = ""
# password = ""

# while username != "Ojas_Amru" and password != "Ojas123":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

# n=int(input("Enter number "))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
# print("Sum is:", sum)


# name = "Ojas"

# newname = " "

# for i in name:
#     if i not in newname:
#         newname+=i

# print(name)
# print(newname)

# #wap a program to reverse the string
# reversed_name = name[::-1]
# print("Reversed string:", reversed_name)


# mycart =[10,20,200,300,800,60,700]
# for i in mycart:
#     if i > 400:
#         print("This is my purchased item:", i)
#         continue
#     print(i)

# user_input = input("Enter a string: ")
# if user_input == user_input[::-1]:
#     print(f"{user_input} is a palindrome")
# else:
#     print(f"{user_input} is not a palindrome")


# str1 = input("Enter first string: ")
# str2 = input("Enter second string: ")
    
# if sorted(str1) == sorted(str2):
#         print(f"{str1} and {str2} are anagrams")
# else:
#         print(f"{str1} and {str2} are not anagrams")


# my_dict = {}
# key = input("Enter key: ")
# value = input("Enter value: ")
# my_dict[key] = value
# print("Dictionary:", my_dict)

# def remove_key(my_dict, key):
#     if key in my_dict:
#         del my_dict[key]
#         print(f"Removed key '{key}' from dictionary.")
#     else:
#         print(f"Key '{key}' not found in dictionary.")

# # Example usage:
# remove_key(my_dict, key)
# print("Dictionary after removal:", my_dict)
# # Check if a key exists in the dictionary
# check_key = input("Enter key to check: ")
# if check_key in my_dict:
#     print(f"Key '{check_key}' exists in the dictionary.")
# else:
#     print(f"Key '{check_key}' does not exist in the dictionary.")


#     print("Iterating over dictionary keys and values:")
#     for k, v in my_dict.items():
#         print(f"Key: {k}, Value: {v}")



#nested for loop

# for i in range(1,4):
#     for j in range(1,4):
#         print(f"i: {i}, j: {j}")

        
# Print a pattern using nested for loops
# for i in range(1, 4):
#             for j in range(1, 4):
#                 print(i, end=' ')
#             print()


# n=int(input("Enter number of rows: "))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(chr(64 + j), end=' ')
#     print()

n=int(input("Enter number of rows: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(n+1-i, end=' ')
    print()




        
