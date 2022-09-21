# TODO: Create auto-letters using letter.txt with the names using names.txt
# If necessary, change the paths for the .txt files

# Here you can change the path
with open('names.txt', 'r') as inv_names_file:
    temp_name_list = inv_names_file.readlines()

name_list = [name.replace('\n', '') for name in temp_name_list if '\n' in name]
name_list.append(temp_name_list[-1])

# Here you can change the path
with open('letter.txt', 'r') as letter_file:
    letter_text_list = letter_file.readlines()

letter_text = ''
for i in letter_text_list:
    letter_text += i

for name in name_list:
    # Here the path is for the newly created letters, you can change the path if you want to create them in somewhere else
    with open(f'ReadyToSend/letter_for_{name}.txt', 'x') as named_letter_file:
        named_letter_file.write(letter_text.replace('[name]', name))

