block_map = [['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️'], ['⬜️', '⬜️', '⬜️']]

print(block_map[0])
print(block_map[1])
print(block_map[2])

digit = input(
    "Enter a two digit number: \n1st digit specifies the column of the map and second digit specifies row of the map: ")

col_num = int(digit[0]) - 1
row_num = int(digit[1]) - 1

block_map[row_num][col_num] = 'X'

print(block_map[0])
print(block_map[1])
print(block_map[2])

# Another Method ==>
'''
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

col_num = int(position[0]) - 1
row_num = int(position[1]) - 1

map[row_num][col_num] = 'x'


#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
'''
