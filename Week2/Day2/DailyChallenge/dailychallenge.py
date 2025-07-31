#DailyChallenge
#Instructions: You are given a “Matrix” string:
#Step 1: Make a 2D List

MATRIX_STR = '''
7ir
Tsi
h%x
i ?
sM# 
$a 
#t%'''       
#clean it up
MATRIX_CLEAN = MATRIX_STR.strip().split('\n')
print(MATRIX_CLEAN)

#create an empty list and take each line and put it in!
matrix_list =[]
for row in MATRIX_CLEAN:
    nested_list = list(row)
    matrix_list.append(nested_list)

for row in matrix_list:
    print(row)

#ensure Neo can read it!
row_numbers=len(matrix_list)
column_numbers=len(matrix_list[0])

for column in range(column_numbers):
    for row in range(row_numbers):
        print(matrix_list[row][column],end=' ')
    print()

#select alpha characters
alphabet_only =[]
for column in range(column_numbers):
    for row in range(row_numbers):
        char = matrix_list[row][column]
        if char.isalpha():
            alphabet_only.append(char)

print(alphabet_only)

#replace symbols
matrix_decoded = []
replace_symbols = ' '

for column in range(column_numbers):
    for row in range(row_numbers):
        char = matrix_list[row][column]
        if char.isalpha():
            matrix_decoded.append(char)
        else:
                matrix_decoded.append(replace_symbols)
print(matrix_decoded)

#clean it up again
final_code =' '.join(''.join(matrix_decoded).split())
print(final_code)