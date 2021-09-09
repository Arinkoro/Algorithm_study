from tkinter import filedialog
import shutil

def main():
    file_from = filedialog.askopenfilename()
    name_list = file_from.split("/")
    old_num = name_list[-1].split(".")[0][-1]
    new_num = "{:03}".format(int(old_num) + 1)
    name_list[-1] = name_list[-1].replace(old_num, new_num)
    file_to = "/".join(name_list)

    # shutil.copyfile(file_from, file_to)
    print(file_to)
    print(file_from)

if __name__ == '__main__':
    main()