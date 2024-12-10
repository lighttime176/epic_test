from DrissionPage import Chromium, ChromiumOptions
import os
import requests
import random
import time
import ddddocr
def logging_init():
  # 创建一个logger对象
  logger = logging.getLogger('my_logger')
  logger.setLevel(logging.INFO)  # 设置日志级别为INFO

  # 创建一个控制台处理器，输出到控制台
  console_handler = logging.StreamHandler()
  console_handler.setLevel(logging.INFO)  # 设置控制台日志级别为INFO

  # 创建一个文件处理器，输出到文件
  file_handler = logging.FileHandler('test.log')
  file_handler.setLevel(logging.INFO)  # 设置文件日志级别为INFO

  # 创建一个日志格式化器
  formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  console_handler.setFormatter(formatter)  # 给控制台处理器设置格式
  file_handler.setFormatter(formatter)  # 给文件处理器设置格式

  # 将控制台和文件处理器添加到logger
  logger.addHandler(console_handler)
  logger.addHandler(file_handler)
  return logger
logger = logging_init()
def random_email():
    account = ''
    randomlength = 15
    base_str = 'qwertyuioplkjhgfdsazxcvbnm0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        account += base_str[random.randint(0, length)]
    logger.info(account)
    return account
co = ChromiumOptions()
co.incognito()
# 用该配置创建页面对象
browser = Chromium(addr_or_opts=co)
tab = browser.latest_tab
for _ in range(10):
    tab.listen.start(targets='captcha')  # 开始监听，指定获取包含该文本的数据包
    tab.get('https://www.serv00.com/offer/create_new_account')
    res = tab.listen.wait().response
    res = res.url
    logger.info(res)
    response = requests.get(res)
    # 检查请求是否成功
    if response.status_code == 200:
        # 打开一个文件并将图片内容写入
        with open("example.jpg", "wb") as file:
            file.write(response.content)
        logger.info("图片下载并保存成功!")
    else:
        logger.info("下载失败，状态码：", response.status_code)
    firstname = random_email()
    ele = tab.ele('css=#id_first_name')
    ele.input(firstname)

    firstname = random_email()
    ele = tab.ele('css=#id_last_name')
    ele.input(firstname)

    firstname = random_email()
    ele = tab.ele('css=#id_username')
    ele.input(firstname)

    ele = tab.ele('css=#id_email')
    ele.input('luo1764682172@gmail.com')

    ocr = ddddocr.DdddOcr()
    ocr.set_ranges(2)
    image = open("example.jpg", "rb").read()
    result = ocr.classification(image, probability=True)
    s = ""
    for i in result['probability']:
        s += result['charsets'][i.index(max(i))]

    logger.info(s)

    ele = tab.ele('css=#id_captcha_1')
    #cap = input('输入验证码')
    ele.input(s)
    ele = tab.ele('css=#id_question2')
    ele.input('free')
    ele = tab.ele('css=#id_tos')
    ele.click()
    ele = tab.ele('css=body > section > div > div.columns > div.column.is-half > form > p.control.submit > button')
    ele.click()
    ele = tab.ele('css=body > section > div > div.columns > div.column.is-half > form > p.control.has-error > span',timeout=30)
    logger.info(ele.text)
    if(ele.text == 'Maintenance time. Try again later.'):
        pass
    elif(ele.text == 'Invalid CAPTCHA'):
        pass
    else:
        exit()
