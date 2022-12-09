with open('text.txt', 'r') as file:
    file_data = file.read()

file_data = file_data.replace('word1', 'word2')

with open('text.txt', 'w') as file:
    file.write(file_data)