# coding=gbk
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QMessageBox
import numpy as np
import xlwt
import uuid
import string
import random

#plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
def imagepath(id) :
    return './images/' + id +'.png'
def getUniqueId():
    imgid = uuid.uuid1().hex[:16]
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    imgid  = imgid + ran_str
    return imgid
def getNumberCount(numberlist, averagescorelist):
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['font.family'] = 'sans-serif'
    fig =plt.figure(num=1, figsize=(5.5, 2.9), dpi=100)
    axes = fig.add_subplot(111)
    x = range(len(numberlist))
    xlist = ['0', '0~40', '40~50', '50~60', '60~70', '70~80', '80~90', '90~100']
    colors = ['orangered', 'darksalmon', 'pink', 'blanchedalmond', 'paleturquoise', 'aquamarine', 'springgreen']

    # 条形图
    rect = axes.bar(x, color=colors, height=numberlist, data=numberlist)
    props = {
        'title': '成绩分布图',
        'xlabel': '分段'
    }
    axes.set(**props)
    axes.set_xticklabels(xlist)
    axes.set_ylabel(u'人数')
    for re in rect:
        height = re.get_height()
        axes.text(re.get_x() + re.get_width() / 2, height + 1, str(height), ha="center", va="bottom")

    # 折线图
    ax2 = axes.twinx()
    ax2.set_ylabel(u'平均分')
    x = np.arange(len(xlist))
    ax2.plot(averagescorelist, marker='o', color='cornflowerblue')
    for a, b in zip(x, averagescorelist):
        ax2.text(a, b, str(b),  ha="center", va="bottom", color='cornflowerblue')
    # self.draw()
    #plt.show()
    imgid = getUniqueId()
    plt.savefig(imagepath(imgid))
    plt.cla()
    plt.clf()
    return imgid

def getWordCloud(url):
    wordcloud = WordCloud(font_path='./fonts/simheittf.ttf',  # 字体
                          background_color=None,
                          mode="RGBA",
                          max_words=40,  # 最大显示单词数
                          max_font_size=60,
                          width=550,
                          height=290,
                          )
    # print(''.join(seganswerdoc))
    print('  + 开始作画')
    wordcloud.generate_from_text(url)
    print('  + 作画完成')
    imgid = getUniqueId()
    print('  + 正在保存')
    wordcloud.to_file(imagepath(imgid))
    print('  + 保存成功')
    return imgid

# app = QApplication(sys.argv)
# myWin = childWindow2()
# myWin.show()
# sys.exit(app.exec_())
if __name__ == '__main__':
    from showpage import *
    from PyQt5.QtCore import *
    from PyQt5.QtGui import *
    # plt.use("Qt5Agg")
    from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
    from matplotlib.figure import Figure
    import sys
    url = """台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 自上而下 互联网 价值 是从 平台 长 聪明 能力 抵不过 千万个 草根 蚂蚁 雄兵 集体 智慧 强大 互联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 最早 提出 互联网 思维 百度 公司 创始人 李彦宏 百度 大型 活动 李彦宏 传统产业 老板 企业家 探讨 发展 时 李彦宏 首次 提到 互联网 思维 词 说 企业家 互联网 思维 做 事情 互联网 思维 方式 互联网 方式 想 几年 观念 越来越 企业家 企业 各行各业 各个领域 认可 互联网 思维 词 演变成 多个 解释 互联网 时代 思考 方式 局限 互联网 产品 互联网 企业 指 互联网 指 桌面 互联网 互联网 泛 互联网 未来 网络 形态 跨越 终端设备 台式机 笔记本 平板 手机 手表 眼镜 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 生活 有助于 更好 生活 学习 发展 内容 发现 特别 难懂 学习 生活 太 理论化 内容 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 联网 思维 互联网 数据 云 计算 科技 发展 背景 市场 用户 产品 企业 价值链 商业 生态 审视 思考 方式 关键 三点 一是 平台 理解 二是 草根 尊重 三是 社区化 自上而下 互联网 价值 是从 平台 长 聪明 能力 抵不过 千万个 草根 蚂蚁 雄兵 集体 智慧 强大 qqq 
     ll 生活 有助于 更好 生活 学习 发展 内容 发现 特别 难懂 学习 生活 太 理论化 内容 生活 有助于 更好 生活 学习 发展 内容 发现 特别 难懂 学习 生活 太 理论化 内容 """
    numberlist = [123, 312, 313, 323, 123, 123, 123]
    averagescorelist = [123, 123, 132, 53, 23, 234, 211]
    print(getNumberCount(numberlist, averagescorelist))
