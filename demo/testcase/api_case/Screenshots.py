import time
import keyboard
from PIL import ImageGrab
from aip import AipOcr
import os


def key_word():
    # 1、截取图片
    keyboard.wait(hotkey='alt+a')  # 键盘输入的触发事件
    print("键盘按下了截图快捷键,请开始下一步操作")
    keyboard.wait(hotkey='enter')
    print("截图成功，开始识别文字")
    time.sleep(0.1)  # 因为读取截取内容会有一个延迟，导致读取到的是上一次的截图，这里我们主动延迟
    # 2、将图片保存到电脑上
    image = ImageGrab.grabclipboard()
    image.save('screen.png')  # 将截取的图片进行保存
    # 3、调用百度API识别图片内容
    APP_ID = '18096794'
    API_KEY = '84tfdA7OWDZa9TQjCS0e16qC'
    SECRET_KEY = 'RwtN4cuk7B0OXkHI85DncHW8eQQHmVd5'
    global client
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)  # 生成一个对策
    with open('screen.png', 'rb') as fp:
        image = fp.read()

    #  删除截图文件
    path = r'D:\myframework\utx-master\demo\testcase\battle\screen.png'  # 文件路径
    if os.path.exists(path):  # 如果文件存在
        os.remove(path)
    else:
        print('no such file:%s' % path)  # 则返回文件不存在

    text = client.basicAccurate(image)
    textList = text['words_result']
    for i in textList:
        print(i['words'])
    return key_word()


if __name__ == '__main__':
    key_word()
