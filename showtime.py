# coding=gbk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
import numpy as np
import xlwt
import uuid
import string
import random

plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
def imagepath(id) :
    return './images/' + id +'.png'
def getUniqueId():
    imgid = uuid.uuid1().hex[:16]
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    imgid  = imgid + ran_str
    return imgid
def getNumberCount(numberlist, averagescorelist):

    fig =plt.figure(num=1, figsize=(5.5, 2.9), dpi=100)
    axes = fig.add_subplot(111)
    x = range(len(numberlist))
    xlist = ['0', '0~40', '40~50', '50~60', '60~70', '70~80', '80~90', '90~100']
    # xlist2 = ['0~40', '40~50', '50~60', '60~70', '70~80', '80~90', '90~100']
    colors = ['orangered', 'darksalmon', 'pink', 'blanchedalmond', 'paleturquoise', 'aquamarine', 'springgreen']

    # ����ͼ
    rect = axes.bar(x, color=colors, height=numberlist, data=numberlist)
    props = {
        'title': '�ɼ��ֲ�ͼ',
        'xlabel': '�ֶ�'
    }
    axes.set(**props)
    axes.set_xticklabels(xlist)
    axes.set_ylabel(u'����')
    for re in rect:
        height = re.get_height()
        axes.text(re.get_x() + re.get_width() / 2, height + 1, str(height), ha="center", va="bottom")

    # ����ͼ
    ax2 = axes.twinx()
    ax2.set_ylabel(u'ƽ����')
    x = np.arange(len(xlist))
    ax2.plot(averagescorelist, c='y', marker='o', color='cornflowerblue')
    for a, b in zip(x, averagescorelist):
        axes.text(a, b, str(b),  ha="center", va="top", color='cornflowerblue',rotation=45,)
    # self.draw()
    #plt.show()
    imgid = getUniqueId()
    plt.savefig(imagepath(imgid))
    plt.cla()
    plt.clf()
    return imgid

def getWordCloud(url):
    wordcloud = WordCloud(font_path='./fonts/simheittf.ttf',  # ����
                          background_color=None,
                          mode="RGBA",
                          max_words=40,  # �����ʾ������
                          max_font_size=60,
                          width=550,
                          height=290,
                          )
    # print(''.join(seganswerdoc))
    wordcloud.generate_from_text(url)
    imgid = getUniqueId()
    wordcloud.to_file(imagepath(imgid))
    return imgid

def saveAsExcel(scoredict):
    print('================================')
    print('���ڱ�����excel�ĵ�........')
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('�ɼ�', cell_overwrite_ok=True)
    row0 = ["�ǳ�", "����", "�ɼ�"]
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i])
    cnt = 1
    for key, value in scoredict.items():
        sheet1.write(cnt, 0, key)
        sheet1.write(cnt, 1, value[1])
        sheet1.write(cnt, 2, value[0])
        cnt += 1
    f.save('./ѧ���ɼ���.xls')
    print('����ɹ�������鿴�����ڳ����Ŀ¼�´� ѧ���ɼ���.xls')


# app = QApplication(sys.argv)
# myWin = childWindow2()
# myWin.show()
# sys.exit(app.exec_())
if __name__ == '__main__':
    from showpage import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    from Mainwindow import *
    from terminalshow import *
    # plt.use("Qt5Agg")
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.figure import Figure
    import sys
    url = """̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���϶��� ������ ��ֵ �Ǵ� ƽ̨ �� ���� ���� �ֲ��� ǧ��� �ݸ� ���� �۱� ���� �ǻ� ǿ�� ������ ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ ���� ��� ������ ˼ά �ٶ� ��˾ ��ʼ�� ����� �ٶ� ���� � ����� ��ͳ��ҵ �ϰ� ��ҵ�� ̽�� ��չ ʱ ����� �״� �ᵽ ������ ˼ά �� ˵ ��ҵ�� ������ ˼ά �� ���� ������ ˼ά ��ʽ ������ ��ʽ �� ���� ���� Խ��Խ ��ҵ�� ��ҵ ���и�ҵ �������� �Ͽ� ������ ˼ά �� �ݱ�� ��� ���� ������ ʱ�� ˼�� ��ʽ ���� ������ ��Ʒ ������ ��ҵ ָ ������ ָ ���� ������ ������ �� ������ δ�� ���� ��̬ ��Խ �ն��豸 ̨ʽ�� �ʼǱ� ƽ�� �ֻ� �ֱ� �۾� ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ������ ���� ���� ѧϰ ��չ ���� ���� �ر� �Ѷ� ѧϰ ���� ̫ ���ۻ� ���� ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���϶��� ������ ��ֵ �Ǵ� ƽ̨ �� ���� ���� �ֲ��� ǧ��� �ݸ� ���� �۱� ���� �ǻ� ǿ�� qqq 
     ll ���� ������ ���� ���� ѧϰ ��չ ���� ���� �ر� �Ѷ� ѧϰ ���� ̫ ���ۻ� ���� ���� ������ ���� ���� ѧϰ ��չ ���� ���� �ر� �Ѷ� ѧϰ ���� ̫ ���ۻ� ���� """
    numberlist = [123, 312, 313, 323, 123, 123, 123]
    averagescorelist = [123, 123, 132, 53, 23, 234, 211]
    print(getnumberCount(numberlist, averagescorelist))
