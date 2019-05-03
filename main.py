import webcrawlerrequests
import answerprocessing
import xlwt

def main(argv=None):
    print('请输入讨论区网址')
    url =  input()
    standardAnswer = ''
    with open('standardAnswer.txt', 'r') as file:
        for lines in file:
            standardAnswer += lines
    webcrawlerrequests.getData(url)
    scoredict = answerprocessing.calculate(standardAnswer)
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('成绩', cell_overwrite_ok=True)
    row0 = ["昵称", "姓名", "成绩"]
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i])
    cnt = 1
    for key, value in scoredict.items():
        sheet1.write(cnt, 0, key)
        sheet1.write(cnt, 1, value[1])
        sheet1.write(cnt, 2, value[0])
        cnt += 1
    f.save('test.xls')

if __name__ == '__main__':
    main()
