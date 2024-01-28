line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

letter=position[0].lower() #get only letter
abc = ["a", "b", "c"]
letter_index=abc.index(letter) #if letter == b, index == 1, if a,index ==0
number_index=int(position[1])-1 # position 3 is [2], so 3-1

map[number_index][letter_index]='x'

print(f"{line1}\n{line2}\n{line3}")