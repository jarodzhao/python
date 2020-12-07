
import os


# 根据扩展名查找文件，返回列表
def get_file_list_by_ext(path, file_ext):
    """
    根据扩展名查找路径下的文件，返回文件列表。
    """
    #_list = []
    _dict = {}
    for root, dirs, files in os.walk(path):
        # 如果是 list
        if type(file_ext) is list:
            if len(file_ext) <= 0:
                for file in files:
                    _dict[file]=root
                    #_list.append(os.path.join(root,file))
            else:
                for file in files:
                    for ext in file_ext:
                        if file.count(ext) > 0:
                            _dict[file]=root
                            #_list.append(\os.path.join(root, file))
                
        elif type(file_ext) is str:
        # 如果是 str
            for file in files:
                if len(file_ext) > 0 and file.count(file_ext) > 0:
                    _dict[file]=root
                    #_list.append(os.path.join(root, file))
                elif len(file_ext) <= 0:
                    _dict[file]=root
                    #_list.append(os.path.join(root, file))
        else:
            print("参数类型必须是list或str")
    return _dict


# 列表中查找包含字符项
def str_in_file_list(_list, _str):
    """
    在列表中查找包含指定字符的项
    """
    _new_list = []
    for f in _list:
        if f.count(_str):
            _new_list.append(f)
    return _new_list


# 列表中的文件类型及数量
def type_count_in_file_list(_list):
    """
    统计一个列表中的文件类型及个数
    """
    file_dict = {}
    for fil in _list:
        # 拆分文件名、扩展名
        _fil_name = fil.split('.')
        # 如果没有扩展名
        if len(_fil_name) == 1:
            if _fil_name[0] in file_dict:
                # 扩展名在字典中
                num = file_dict.get(_fil_name[0])
                file_dict[_fil_name[0]] = num + 1
            else:
                # 扩展名不在字典中
                pass
                file_dict[_fil_name[0]] = 1
        else:
            # 有扩展名的
            if _fil_name[1] in file_dict:
                # 在字典中
                num = file_dict.get(_fil_name[1])
                file_dict[_fil_name[1]] = num + 1
            else:
                # 不在字典中
                file_dict[_fil_name[1]] = 1
    return file_dict


if __name__ == '__main__':
    pass
    path = r'.'

    file_exts = ['.py']

    # 路径下的文件列表
    file_list = get_file_list_by_ext(path, file_exts)
    print(len(file_list))
    for d in file_list:
        print(d, "|", file_list[d])
