import os #very useful module for navigating files? 
#Python I/O

#how to read a file

dir_path = os.path.dirname(os.path.realpath(__file__)) #will search directory for file
print('dir path: ', dir_path)

with open(f'{dir_path}/secrets.txt', 'r', encoding='utf-8') as file_obj:
    file_content = file_obj.read()

    print(file_content)

#f.read() 
#f.readline() # Reads one entire line from the file. Reads a file till the newline
#f.readlines() # Reads a file line by line, returns a list of the lines in the file

#f.write(str) 
#f.writelines(seq) # Writes a list of lines to the file.
# Example : 
# lines=["Hello world.\n", "Welcome to Paris.\n"]
# f.writelines(lines)

#f.seek(offset)   #moves cursor to where you want it to be in tehh file
#f.tell() # for binary files, mostly

#f.close()

#STAR WARS EXERCISE
#read the file line by line 
dir_path = os.path.dirname(os.path.realpath(__file__)) #will search directory for file
print('dir path: ', dir_path)

with open(f'{dir_path}/star_wars.txt', 'r', encoding='utf-8') as f:
    txt_list =f.readlines()
    for line in txt_list:
        print(line)
    print('end of document')

    print(file_content)

#read only the 5th line of the file
    #print(txt_list[4])
#read only the 5 first charactrs of the file
#print(txt_list[0][:4])

#read all the file and return it as a list of strings. thens plit each word as a letter
#using list comprehension (make sure its easy not too complex)

#temp = [line.split() for line in txt_list]
#temp = [list(line) for line in txt_list]
#print(temp)

#find out occurrences of Darth Luke and Lea
counts = {'Darth':0, 'Luke': 0, 'Lea':0}
for line in txt_list:
    line=line.strip()
    if line == 'Darth':
        counts['Darth']+= 1
    elif line == 'Luke':
        counts['Luke']+= 1
    elif line == 'Lea':
        counts['Lea']+= 1
print(counts)

#append your name to the end of the file

#with open(f'{dir_path}/star_wars.txt', 'a', encoding='utf-8') as f:
    #f.seek(0) #ensures cursor goes to the beginning of the file
    #f.seek(0, os.SEEK_END) #makes sure that the cursor is at the end of the file
    #f.write('\nRachel')
    #print('successfully added')

#append 'Skywalker'next to each first name 'Luke
#for i, name in enumerate(txt_list):
#    if name.strip() == 'Luke':
#        txt_list[i] = f'{name} Skywalker'
#print('Copy that')
#NOT WORKING BECAUSE we CANNOT CHANGE OBJECT FILE DIRECTLY. YOU NEED TO COPY
#THE CONTENT, CHANGE IT AND THEN OVERWRITE THE CONTENT

modified_lines = []
for line in txt_list:
    if line.strip() == 'Luke':
        modified_lines.append('Luke Skywalker\n')
    else:
        modified_lines.append(line)

with open(f'{dir_path}/star_wars.txt', 'w', encoding='utf-8') as f:
    f.seek(0) #make sure the cursor is at the beginning of the file
    f.writelines(modified_lines)
