"""
#目的:判断两个Excel表数据是否一致，不一致则打印出范围
#作者:caoqq
#日期:20200316
"""
import xlrd

class Data_Excel():
    def __init__(self,file_add1,file_add2):
        self.list1 = []
        self.list2 = []
        self.file_add1 = file_add1
        self.file_add2 = file_add2

    def open_excel(self):
        try:  # 检验文件有没有被获取到
            self.data1 = xlrd.open_workbook(self.file_add1)
            self.data2 = xlrd.open_workbook(self.file_add2)
            return self.data1,self.data2
        except Exception:
            print('文件地址错误！')
            print('error!')

    def operate_excel(self,data1,data2):
        table1 = data1.sheets()[0]       #获取sheet表
        table2 = data2.sheets()[0]  # 获取sheet表


        for i in range(0,table1.nrows):
            value = table1.row_values(i, start_colx=0, end_colx=None)
            self.list1.append(value)

        for i in range(0,table2.nrows):
            value = table2.row_values(i, start_colx=0, end_colx=None)
            self.list2.append(value)

        return self.list1,self.list2

    def is_same(self,list1,list2):
        if len(list1) != 0 and len(list2) != 0:
            flag = 0
            table1 = data1.sheets()[0]  # 获取sheet表
            table2 = data2.sheets()[0]  # 获取sheet表

            if table1.nrows == table2.nrows and table1.ncols == table2.ncols:
                for i in range(len(list1)):
                   for j in range(len(list1[i])):
                       if list1[i][j] != list2[i][j]:
                           flag = 1
                           print(i,j)
                if flag == 0:
                    print("两个Excel一致!")
            else:
                print("两个Excel不一致!")
        else:
            print("存在空工作簿")
        return

if __name__ == '__main__':

    file1 = r'C:\Users\10003144\Desktop\test.xlsx'
    file2 = r'C:\Users\10003144\Desktop\test1.xlsx'
    data = Data_Excel(file1,file2)
    data1,data2=data.open_excel()
    list1,list2 = data.operate_excel(data1,data2)
    data.is_same(list1,list2)
