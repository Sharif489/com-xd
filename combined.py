files = []
file = int(input('how many files :'))
for x in range(file):
    filrs= input(f'name of {x} file : ')
    files.append(filrs)



save = input(' save file : ')
all_lines = []

for file_name in files:
    with open(file_name, 'r') as file:
        lines = file.readlines()
        all_lines.extend(lines)

with open(save, 'w') as combined_file:
    combined_file.writelines(all_lines)

print(f'All files have been combined into {save}')