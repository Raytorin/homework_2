from pprint import pprint

def read_file(file1, count1):
    i = 0
    list_book = []
    while i <= count1:
        line = file1.readline().split(' | ')
        i += 1
        if len(line) == 3:
            list_book.append({'ingredient_name': line[0],'quantity': line[1], 'measure': line[2].strip('\n')})
    return list_book

def counte(count2):
    i = 0
    while i <= count2:
        i += 1
    u = i + 2
    return u

with open('data_1.txt', encoding='utf-8') as f:
    cook_book = {}
    all_count = len(f.readlines())
    correct_count = 0
    f.seek(0)
    while correct_count <= all_count:
        name = f.readline().strip('\n')
        count = int(f.readline())
        cook_book[name] = read_file(f, count)
        correct_count += counte(count)

    pprint(cook_book, sort_dicts=False)