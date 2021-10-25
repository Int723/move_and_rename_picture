import os
import shutil


def move_picture(in_path, out_path):

    dh = []  # 所有照片存放的路径集合 
    sh = []  # 所有使用人照片存放的路径集合
    sh1 = []  # 所有使用人配偶照片存放的路径集合
    f = []  # 所有照片文件集合

    for home, dirs, filenames in os.walk(out_path):
        if "正元房地一体" in home and "Y_zjh" in home:  # 找到照片存放的文件夹位置
            dh.append(home)
            # lis = home.split('\\')
            # print(lis[-2][:-2])

    for home, dirs, filenames in os.walk(in_path):
        if "申请人身份证明" in home:  # 找使用人照片文件需要存放的位置
            sh.append(home)
        if "家庭成员" in home and '户口本' in home:  # 找到使用人配偶照片需要存放的位置
            sh1.append(home)
        for filename in filenames:
            if "使用人" in filename and "国徽面" in filename and "配偶" not in filename:
                f.append(filename)

    for i in dh:
        path2 = os.path.join(i,'使用人身份证人像面.jpg')
        path3 = os.path.join(i,'使用人身份证国徽面.jpg')
        path4 = os.path.join(i,'使用人配偶身份证人像面.jpg')
        path5 = os.path.join(i,'使用人配偶身份证国徽面.jpg')
        lis = i.split('\\')
        coder = lis[-2][:-2]  # 每个人的文件夹名去掉最后一位数字
        for j in sh:
            if coder in j:
                try:
                    shutil.copy(path2, os.path.join(j,'test.jpg'))
                except FileNotFoundError:
                    print('无法找到照片文件，请核对文件'+path2+'名称是否正确')
                try:
                    shutil.copy(path3,os.path.join(j, 'test1.jpg'))
                except FileNotFoundError:
                    print('无法找到照片文件，请核对文件'+path3+'名称是否正确')

        for j in sh1:
            if coder in j:
                try:
                    shutil.copy(path4, os.path.join(j,'test.jpg'))
                except FileNotFoundError:
                    print('无法找到照片文件，请核对文件'+path4+'名称是否正确'+'\n'+'如无使用人配偶身份证照片则忽略此条信息')
                try:
                    shutil.copy(path5,os.path.join(j, 'test1.jpg'))
                except FileNotFoundError:
                    print('无法找到照片文件，请核对文件'+path5+'名称是否正确'+'\n'+'如无使用人配偶身份证照片则忽略此条信息')


inpath = "F:\\00软件项目\\昌乐模板\\苍穹软件模板"
outpath = "F:\\00软件项目\\昌乐模板\\正元房地一体软件模板"
move_picture(inpath, outpath)
