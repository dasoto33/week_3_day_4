# Pair of Gloves

# Winter is approaching, and you are preparing for your ski holidays. Your task is to determine the number of pairs
# of gloves you can create from the gloves in your drawer.

# Given an array describing the color of each glove, your goal is to calculate the number of pairs you can make. 
# Remember, only gloves of the same color can form pairs.

# Write a function that takes in the array of glove colors and returns the number of pairs that can be constituted.

# Examples:

# Input 1:
["red", "green", "red", "blue", "blue"]
# Output 1:
# Explanation:
# You can form 1 pair of red gloves and 1 pair of blue gloves.

# Input 2:
["red", "red", "red", "red", "red", "red"]
# Output 2:
# Explanation:
# You can form 3 pairs of red gloves.

# Steps:
# 1. count the occurences of each color
# 2. filter out those that dont form a pair

# Solution 1:


def glove_pairs(gloves):
    glove_count = {}
    for glove in gloves:
        if glove in glove_count:
            glove_count[glove] += 1
        else:
            glove_count[glove] = 1
    
    return len(list(filter(lambda x: glove_count[x] == 2, glove_count.keys())))

gloves1 = ["red", "green", "red", "blue", "blue"]
print(glove_pairs(gloves1))


# Solution 2:

def find(color_list):
    output, pair_list = 0, {} #color count
    for glove in gloves:
       glove_pairs[glove] = glove_pairs.get(glove, 0) + 1
       if glove_pairs[glove] == 2:
                  output += 1


