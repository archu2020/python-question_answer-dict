dictionary={"1":"Ans: A namespace is a naming system used to make sure that names are unique to avoid naming conflicts.",
            "2": "Ans: It is an environment variable which is used when a module is imported.\n"
                   "Whenever a module is imported, PYTHONPATH is also looked up to check for the\n"
                   "presence of the imported modules in various directories.\n"
                    "The interpreter uses it to determine which module to load.",
            "3":"Global Variables:\n"
                "Variables declared outside a function or in global space are called global variables.\n"
                "These variables can be accessed by any function in the program.\n"
                "Local Variables:\n"
                "Any variable declared inside a function is known as a local variable. This variable is present in the\n"
                "local space and not in the global space.",
            "4":"Ans: Yes. Python is a case sensitive language.",
            "5":"Ans: Type conversion refers to the conversion of one data type iinto another.",
            "6":"Ans: Indentation is necessary for Python. "
                "It specifies a block of code. All code within loops, classes, functions,\n"
                "etc is specified within an indented block. It is usually done using four space characters.\n"
                "If your code is not indented necessarily, it will not execute accurately and will throw errors as well."
            }
# dictionary = dict()
# data = input('Enter Question & Answer separated by ":" ')
# temp = data.split(':')
# dictionary[temp[0]] = int(temp[1])
#
# # Displaying the dictionary
# for key, value in dictionary.items():
#     print(': {}, Answer: {}'.format(key, value))
#print(dictionary["5"])
# inp=input("Please Enter your Question.")
print("1. What is namespace in Python?","press 1")
print("2. What is PYTHONPATH?","press 2")
print("3. What are local variables and global variables in Python?","press 3")
print("4. Is python case sensitive?","press 4")
print("5. What is type conversion in Python?","press 5")
print("6. Is python case sensitive?","press 6\n")
qus=6
no_qus=0

while(no_qus<6):

    inp=input("Please Enter your Question Number.\n")

    if inp == "1":
        print("What is namespace in Python?")
        print(dictionary["1"])
        print()

    elif inp == "2":
        print("What is PYTHONPATH?")
        print(dictionary["2"])
        print()

    elif inp == "3":
        print("What are local variables and global variables in Python?")
        print(dictionary["3"])
        print()

    elif inp == "4":
        print("Is python case sensitive?")
        print(dictionary["4"])
        print()

    elif inp == "5":
        print("What is type conversion in Python?")
        print(dictionary["5"])
        print()

    elif inp == "6":
        print("Is python case sensitive?")
        print(dictionary["6"])
        print()



