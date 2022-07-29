import os

FILE_NAME_1 = '1.txt'
FILE_NAME_2 = '2.txt'
FILE_NAME_3 = '3.txt'
FILE_PATH = 'sorted'
ROOT_PATH = os.getcwd()
full_path_1 = os.path.join(ROOT_PATH, FILE_PATH, FILE_NAME_1)
full_path_2 = os.path.join(ROOT_PATH, FILE_PATH, FILE_NAME_2)
full_path_3 = os.path.join(ROOT_PATH, FILE_PATH, FILE_NAME_3)

list1 = []
dict1 = {}
sorted_dict = {}


class File:
    def __init__(self, file_path):
        self.file_path = file_path
        self.name = os.path.basename(self.file_path)

    def content(self):
        with open(self.file_path, encoding='utf_8') as file:
            content_list = file.read()
            # for i in content_list:
            #     print(i.strip())
        return content_list.rstrip()

    def __length(self):
        with open(self.file_path, encoding='utf_8') as file:
            content_list = file.readlines()
            return len(content_list)

    def add_in_dict(self):
        list2 = []
        list2.append(self.__length())
        list2.append(self.content())
        list1.append(list2)
        dict1[self.name] = list2
        return


file1 = File(full_path_1)
file2 = File(full_path_2)
file3 = File(full_path_3)

file1.content()
file2.content()
file3.content()

file1.add_in_dict()
file2.add_in_dict()
file3.add_in_dict()
sorted_keys = sorted(dict1, key=dict1.get)


def sorted(dict):
    for w in sorted_keys:
        sorted_dict[w] = dict1[w]
    for key, value in sorted_dict.items():
        print(key)
        for v in value:
            print(v)


sorted(sorted_dict)
