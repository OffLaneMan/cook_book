import os

file1 = "1.txt"
file2 = "2.txt"
file3 = "3.txt"
files = [file1, file2, file3]


def итоговый_файл(files):
    f_list = []
    for f in files:
        with open(os.path.join(os.path.dirname(__file__), "files", f),encoding='utf-8') as file:
                f_list.append([f, file.readlines()])
    f_list.sort(key=lambda x: len(x[1]))
    with open(os.path.join(os.path.dirname(__file__), "files", "итоговый_файл.txt"), "w", encoding='utf-8') as file:
        for f in f_list:
            file.write(f[0] + '\n')
            file.write(str(len(f[1])) + '\n')
            file.writelines(f[1])
            file.write('\n')



итоговый_файл(files)