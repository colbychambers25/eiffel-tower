###
### Author: Colby Chambers
### Course: CSC 110
### Description: Print the Eiffel Tower with using a user input
###              to determine the size by expanding
###              all elements proportionally.
###

size = int(input('Enter Eiffel tower size:\n'))

# The formulas for each sections expansion.
upper_width=3
upper_height= size*1.5
mid_width= size*2+1
mid_height=size/2+3
low_width=size*4+1
low_height= size/1.5

# The formulas for the space between the middle and upper sections.
space_upper = ((low_width-upper_width+4)/2)
space_mid = ((low_width-mid_width+4)/2)

# Each lines inital variable before multiplying by the input.
# Also, performs the multiplication that sets
# the majority of the spacing for the tower.
top_vert = int(space_upper)*' '+' '+'|Z|\n'
top_hori = 'Z'
mid_vert = int(space_mid)*' '+'H'+mid_width*' '+'H\n'
mid_hori = '%'
low_hori = ' ##'+low_width*' '+'## \n'
low_vert = '## '+low_width*' '+' ##\n'

#the lines after applying the variables created above and multiplying them by the input.
print()
print(int(space_upper)*' '+'  '+'$')
print(top_vert*int(upper_height),end='')
print(int(space_mid)*' '+'/'+top_hori*mid_width+'\ ')
print(mid_vert*int(mid_height), end='')
print('  '+'/'+mid_hori*low_width+'\ ')
print(low_hori*int(low_height),end='')
print(low_vert*int(low_height),end='')
