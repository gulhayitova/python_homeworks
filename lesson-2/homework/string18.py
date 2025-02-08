string = input("Input: ").split()
start = input("Starts with: ")
end = input("Ends with: ")
print(bool(string[0] == start and string[-1] == end))