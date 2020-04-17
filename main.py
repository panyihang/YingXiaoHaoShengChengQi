import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from functools import partial
import ui

def 营销号生成(ui):
    主题  = str(ui.textEdit_4.toPlainText())
    内容  = str(ui.textEdit_6.toPlainText())
    另一个说法 = str(ui.textEdit_5.toPlainText())
    if len(主题)==0 or len(内容)==0 or len(另一个说法)==0:
        pass 
    else:
        结果  = '%s%s是怎么回事呢？%s相信大家都很熟悉，但是%s%s是怎么回事呢，下面就让小编带大家一起了解吧。\n%s%s，其实就是%s，大家可能会很惊讶%s怎么会%s呢？但事实就是这样，小编也感到非常惊讶。\n这就是关于%s的事情了，大家有什么想法呢，欢迎在评论区告诉小编一起讨论哦！' % (主题,内容,主题,主题,内容,主题,内容,另一个说法,主题,内容,主题)
        ui.textEdit.setText(str(结果))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = ui.Ui_Form()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.pushButton.clicked.connect(partial(营销号生成, ui))
    sys.exit(app.exec_())
    
