import os


def main():
    # 1 获取用户要copy的文件夹名字
    old_folder_name = input("请输入要copy的文件夹的名字：")

    # 2 创建一个新的文件夹
    os.mkdir(old_folder_name + "[复制]")

    # 3 获取文件夹的所有的待copy的文件名字  listdir()
    file_names = os.listdir(old_folder_name)
    print(file_names)

    # 4 创建进程池
    # 5 复制源文件夹中的文件，到新的文件夹中的文件去


if __name__ == '__main__':
    main()