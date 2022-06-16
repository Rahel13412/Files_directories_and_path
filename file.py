file = open("my_file.txt")  # open a file
contents = file.read()  # read the file content
print(contents)
file.close()  # close the file

with open("my_file.txt") as file:  # another way to open a file
    contents = file.read()
    print(contents)

with open("my_file.txt", mode="w") as file:
    file.write("new notes")   # delete everything from file and write "new notes"

with open(file="my_file.txt",mode="a") as file:
    file.write("\nmy name is rahel")   # append the text


with open ("new_file.txt",mode="w") as new_file:   # if the file does not exit then it will create one.
    new_file.write("my sister name is Tamanna!")


