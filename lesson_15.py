def write_file(file, text):
    file = open(file, 'w')
    file.write(text)
    file.close()


def update_file(file, text):
    file = open(file, 'a')
    file.write(text)
    file.close()


def read_file(file):
    file = open(file, 'r')
    return file.read()


def average_grades(file):
    content = read_file(file)
    sudent_notes = content.split('\n')
    list_average = []
    for x in sudent_notes:
        list_notes = x.split(',')
        sudent = list_notes[0]
        list_notes.pop(0)
        average = lambda notes: sum([int(i) for i in notes]) / 4
        list_average.append({sudent, average(list_notes)})
    return list_average

if __name__ == '__main__':
    # write_file('files/test.txt', 'Primeira linha')
    # update_file('files/test.txt', '\nSegunda linha')
    # print(read_file('files/test.txt'))
    print(average_grades('files/notes.txt'))
