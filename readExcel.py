import xlrd
import os


def sorted_dict(adict): 
    items = adict.items() 
    items.sort() 
    return [value for key, value in items]

if __name__=="__main__":
    print("-"*50)
    
    # 当前路径
    fp=os.path.split(os.path.realpath(__file__))
    
    #excel文档
    xfile=xlrd.open_workbook(fp[0]+"/2st.xlsx")
    #print(xfile)
    
    #数据表格
    table=xfile.sheets()[0]
    rows=table.nrows
    
    dict0={}
    #遍历组装成字典
    for i in range(rows):
        fn4=table.row_values(i)[4]
        fn5=table.row_values(i)[5]
        if len(fn5)<5:
            fn5+=" "*10
        #print(fn5,	"\t", fn4)
        dict0[fn5]=fn4
        
    #输出
    for d in dict0:
        print(d)
        
    #排序
    dict2=sorted(dict0.items(), key=lambda d:d[0])
    
    #输出排最后
    for d in dict2:
        print(d)
    print('*'*50)
    
    