#Code 01: 
# words is an array a variable in which one stores multiple data objects
words = []
# num str is a variable that collects input  and puts in an int
num_str = input("How many words would you like to enter?")
#converting the num string into an int 
num = int(num_str)
# a for loop transforming the num variable to count how many times it must run
for _ in range(0,num):
 #running words  as an act.
    word = input("Next word:")
    words.append(word)
print("This is your list of words:",words)