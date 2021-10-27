"""
You probably know the "like" system from Facebook and other pages. People can "like" blog posts, pictures or other items. We want to create the text that should be displayed next to such an item.

Implement the function which takes an array containing the names of people that like an item. It must return the display text as shown in the examples:

[]                                -->  "no one likes this"
["Peter"]                         -->  "Peter likes this"
["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"
"""
names = ["Alex", "Jacob", "Mark", "Max"]
names1 = ["Peter"]
names2 = ["Jacob", "Alex"]
names3 = ["Max", "John", "Mark"]
none = ""

def likes(names):
    
    if len(names) <= 3:
        if len(names) == 0:
            print("no one likes this")
        elif len(names) == 1:
            print(f"{names[0]} likes this")
        elif len(names) == 2:
            print(f"{names[0]} and {names[1]} like this")            
        else:
            print(f"{names[0]}, {names[1]} and {names[2]} like this")
    else:
        print(f"{names[0]}, {names[1]} and {len(names)-2} others like this")



likes(names)
