
first_file_name = input("Please enter the first file name including .txt (must be in the directory)")
second_file_name = input("Please enter the second file name including .txt (must be in the directory")

print("Are these correct? Y/N", first_file_name, second_file_name)

response = input()

if response == 'y':

    with open(first_file_name, 'r') as file1:

        with open(second_file_name, 'r') as file2:
            same = set(file1).intersection(file2)

    same.discard('\n')

    with open('results.txt', 'w') as file_out:
        for line in same:
            file_out.write(line)

    num_lines = sum(1 for line in open('results.txt'))
    print("Number of zombie accounts are ", num_lines)

elif response == 'n':
    print ("u ok hun")
    exit()
