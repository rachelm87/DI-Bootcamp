#Write code that will ask the user for their height in centimeters.

your_height = input("Please tell me your height in CM ")
your_height =int(your_height)

#now determine if they can ride it!
if your_height > 145:
    print ("You are tall enough to ride this ride!")
else: 
    print ("Sorry Charlie! Gotta grow some more!") 
