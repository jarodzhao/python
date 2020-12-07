import fileUtils as fu


def get_list():
    ext = []
    path = "/storage/emulated/0/1"
    _list=fu.get_file_list_by_ext(path, ext)
    for f in _list:
        print(f, "\n", _list[f], "\n")


if __name__=="__main__":
    get_list()

    #count=fu.type_count_in_file_list(files)
    #print(count)