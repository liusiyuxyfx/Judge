# coding=gbk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
from Mainwindow import *
from terminalshow import *
#plt.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from showpage import *
import sys

url = """̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���϶��� ������ ��ֵ �Ǵ� ƽ̨ �� ���� ���� �ֲ��� ǧ��� �ݸ� ���� �۱� ���� �ǻ� ǿ�� ������ ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ ���� ��� ������ ˼ά �ٶ� ��˾ ��ʼ�� ����� �ٶ� ���� � ����� ��ͳ��ҵ �ϰ� ��ҵ�� ̽�� ��չ ʱ ����� �״� �ᵽ ������ ˼ά �� ˵ ��ҵ�� ������ ˼ά �� ���� ������ ˼ά ��ʽ ������ ��ʽ �� ���� ���� Խ��Խ ��ҵ�� ��ҵ ���и�ҵ �������� �Ͽ� ������ ˼ά �� �ݱ�� ��� ���� ������ ʱ�� ˼�� ��ʽ ���� ������ ��Ʒ ������ ��ҵ ָ ������ ָ ���� ������ ������ �� ������ δ�� ���� ��̬ ��Խ �ն��豸 ̨ʽ�� �ʼǱ� ƽ�� �ֻ� �ֱ� �۾� ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ������ ���� ���� ѧϰ ��չ ���� ���� �ر� �Ѷ� ѧϰ ���� ̫ ���ۻ� ���� ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���� ˼ά ������ ���� �� ���� �Ƽ� ��չ ���� �г� �û� ��Ʒ ��ҵ ��ֵ�� ��ҵ ��̬ ���� ˼�� ��ʽ �ؼ� ���� һ�� ƽ̨ ��� ���� �ݸ� ���� ���� ������ ���϶��� ������ ��ֵ �Ǵ� ƽ̨ �� ���� ���� �ֲ��� ǧ��� �ݸ� ���� �۱� ���� �ǻ� ǿ�� qqq 
 ll ���� ������ ���� ���� ѧϰ ��չ ���� ���� �ر� �Ѷ� ѧϰ ���� ̫ ���ۻ� ���� ���� ������ ���� ���� ѧϰ ��չ ���� ���� �ر� �Ѷ� ѧϰ ���� ̫ ���ۻ� ���� """
def getWordCloud(str):
    wordcloud = WordCloud(font_path='./fonts/simheittf.ttf',  # ����
                          background_color=None,
                          mode="RGBA",
                          max_words=40,  # �����ʾ������
                          max_font_size=60,
                          width=579,
                          height=294
                          )
    # print(''.join(seganswerdoc))
    wordcloud.generate_from_text(''.join(str))

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

class Figure_Canvas(FigureCanvas):   # ͨ���̳�FigureCanvas�࣬ʹ�ø������һ��PyQt5��Qwidget������һ��matplotlib��FigureCanvas����������pyqt5��matplot                                          lib�Ĺؼ�

    def __init__(self, parent=None, width=5.5, height=2.9, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # ����һ��Figure��ע�⣺��FigureΪmatplotlib�µ�figure������matplotlib.pyplot�����figure
        FigureCanvas.__init__(self, fig) # ��ʼ������
        self.setParent(parent)

        self.axes = fig.add_subplot(111) # ����figure�����add_subplot������������matplotlib.pyplot�����subplot����

    def wordlist(self, url):
        wordcloud = WordCloud(font_path='./fonts/simheittf.ttf',  # ����
                              background_color=None,
                              mode="RGBA",
                              max_words=40,  # �����ʾ������
                              max_font_size=60,
                              width=560,
                              height=300
                              )
        # print(''.join(seganswerdoc))
        print(wordcloud.generate_from_text(url))
        self.axes.imshow( wordcloud.generate_from_text(url))
        self.axes.axis("off")

    def numberCount(self, dict):#dict{�ֶ�:[����������]}
        plt.rcParams['font.sans-serif'] = ['SimHei']
        xlist = list(dict.keys())
        y1list = list(value[0] for value in dict.values())
        y2list = list(value[0] for value in dict.values())



        #
class childWindow2(QDialog, Ui_Dialog_showpage):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)


        dr = Figure_Canvas()
        #ʵ����һ��FigureCanvas
        dr.test()  # ��ͼ
        graphicscene = QtWidgets.QGraphicsScene() # ������������һ��QGraphicsScene����Ϊ���ص�ͼ�Σ�FigureCanvas������ֱ�ӷŵ�graphicview�ؼ��У������ȷŵ�graphicScene��Ȼ���ٰ�graphicscene�ŵ�graphicview��
        #graphicscene.setGeometry(QtCore.QRect(630, 80, 561, 301))
       # graphicscene.fi
        graphicscene.addWidget(dr)  # ���Ĳ�����ͼ�ηŵ�QGraphicsScene�У�ע�⣺ͼ������Ϊһ��QWidget�ŵ�QGraphicsScene�е�
        #graphicscene.
        self.graphicsView_wordcloud.setScene(graphicscene)  # ���岽����QGraphicsScene����QGraphicsView
        self.graphicsView_wordcloud.show()  # ��󣬵���show��������ͼ�Σ�Voila!!

app = QApplication(sys.argv)
myWin = childWindow2()
myWin.show()
sys.exit(app.exec_())

