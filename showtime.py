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

url = """台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 自上而下 互联网 价值 是从 平台 长 聪明 能力 抵不过 千万个 草根 蚂蚁 雄兵 集体 智慧 强大 互联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 最早 提出 互联网 思维 百度 公司 创始人 李彦宏 百度 大型 活动 李彦宏 传统产业 老板 企业家 探讨 发展 时 李彦宏 首次 提到 互联网 思维 词 说 企业家 互联网 思维 做 事情 互联网 思维 方式 互联网 方式 想 几年 观念 越来越 企业家 企业 各行各业 各个领域 认可 互联网 思维 词 演变成 多个 解释 互联网 时代 思考 方式 局限 互联网 产品 互联网 企业 指 互联网 指 桌面 互联网 互联网 泛 互联网 未来 网络 形态 跨越 终端设备 台式机 笔记本 平板 手机 手表 眼镜 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 生活 有助于 更好 生活 学习 发展 内容 发现 特别 难懂 学习 生活 太 理论化 内容 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 自上而下 互联网 价值 是从 平台 长 聪明 能力 抵不过 千万个 草根 蚂蚁 雄兵 集体 智慧 强大 qqq 
 ll 生活 有助于 更好 生活 学习 发展 内容 发现 特别 难懂 学习 生活 太 理论化 内容 生活 有助于 更好 生活 学习 发展 内容 发现 特别 难懂 学习 生活 太 理论化 内容 """
def getWordCloud(str):
    wordcloud = WordCloud(font_path='./fonts/simheittf.ttf',  # 字体
                          background_color=None,
                          mode="RGBA",
                          max_words=40,  # 最大显示单词数
                          max_font_size=60,
                          width=579,
                          height=294
                          )
    # print(''.join(seganswerdoc))
    wordcloud.generate_from_text(''.join(str))

    plt.imshow(wordcloud)
    plt.axis("off")
    plt.show()

class Figure_Canvas(FigureCanvas):   # 通过继承FigureCanvas类，使得该类既是一个PyQt5的Qwidget，又是一个matplotlib的FigureCanvas，这是连接pyqt5与matplot                                          lib的关键

    def __init__(self, parent=None, width=5.5, height=2.9, dpi=100):
        fig = Figure(figsize=(width, height), dpi=100)  # 创建一个Figure，注意：该Figure为matplotlib下的figure，不是matplotlib.pyplot下面的figure
        FigureCanvas.__init__(self, fig) # 初始化父类
        self.setParent(parent)

        self.axes = fig.add_subplot(111) # 调用figure下面的add_subplot方法，类似于matplotlib.pyplot下面的subplot方法

    def wordlist(self, url):
        wordcloud = WordCloud(font_path='./fonts/simheittf.ttf',  # 字体
                              background_color=None,
                              mode="RGBA",
                              max_words=40,  # 最大显示单词数
                              max_font_size=60,
                              width=560,
                              height=300
                              )
        # print(''.join(seganswerdoc))
        print(wordcloud.generate_from_text(url))
        self.axes.imshow( wordcloud.generate_from_text(url))
        self.axes.axis("off")

    def numberCount(self, dict):#dict{分段:[人数，均分]}
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
        #实例化一个FigureCanvas
        dr.test()  # 画图
        graphicscene = QtWidgets.QGraphicsScene() # 第三步，创建一个QGraphicsScene，因为加载的图形（FigureCanvas）不能直接放到graphicview控件中，必须先放到graphicScene，然后再把graphicscene放到graphicview中
        #graphicscene.setGeometry(QtCore.QRect(630, 80, 561, 301))
       # graphicscene.fi
        graphicscene.addWidget(dr)  # 第四步，把图形放到QGraphicsScene中，注意：图形是作为一个QWidget放到QGraphicsScene中的
        #graphicscene.
        self.graphicsView_wordcloud.setScene(graphicscene)  # 第五步，把QGraphicsScene放入QGraphicsView
        self.graphicsView_wordcloud.show()  # 最后，调用show方法呈现图形！Voila!!

app = QApplication(sys.argv)
myWin = childWindow2()
myWin.show()
sys.exit(app.exec_())

