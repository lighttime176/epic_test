import requests,logging,random,time,ddddocr
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
firstnames = [
    "Liam", "Noah", "Oliver", "Elijah", "James", "William", "Benjamin", "Lucas", "Henry", "Alexander",
    "Mason", "Michael", "Ethan", "Daniel", "Jacob", "Jackson", "Logan", "David", "Joseph", "Samuel",
    "Sebastian", "Jack", "Aiden", "Matthew", "Wyatt", "John", "Leo", "Isaac", "Gabriel", "Julian",
    "Owen", "Luke", "Asher", "Carter", "Grayson", "Zachary", "Ryan", "Nathan", "Samuel", "Leo",
    "Anthony", "Jaxon", "Lincoln", "Joshua", "Christopher", "Andrew", "Theodore", "Caleb", "Christian",
    "Eli", "Aaron", "Hunter", "Jonathan", "Isaiah", "Charles", "Thomas", "Hudson", "Adrian", "Nolan",
    "Ezra", "Maverick", "Eli", "Jordan", "Angel", "Roman", "Miles", "Adam", "Ian", "Robert",
    "David", "Jesse", "Evan", "Bryce", "Cooper", "Miles", "Carson", "Xavier", "Leo", "Avery",
    "Sawyer", "Gavin", "Colton", "Elliott", "Vincent", "Ezekiel", "Giovanni", "Nico", "Toby", "Daniel",
    "Archer", "Blake", "Dominic", "Caden", "Dylan", "Milo", "Camden", "Jude", "Caden", "Omar",
    "Maxwell", "Kingston", "Santiago", "Max", "Seth", "Oscar", "Bennett", "Emmett", "Finn", "Malcolm",
    "Kingston", "Austin", "Bryan", "Zane", "Kai", "Jaden", "Calvin", "Xander", "Finnley", "Judah"
]
lastnames = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
    "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Garcia", "Martinez", "Roberts",
    "Clark", "Rodriguez", "Lewis", "Lee", "Walker", "Hall", "Allen", "Young", "King", "Wright",
    "Scott", "Torres", "Nguyen", "Hill", "Adams", "Baker", "Gonzalez", "Nelson", "Carter", "Mitchell",
    "Perez", "Robinson", "Hernandez", "Graham", "Sanchez", "Green", "Stewart", "Morris", "Rivera", "Cook",
    "Rogers", "Morgan", "Bell", "Murphy", "Bailey", "Cooper", "Richardson", "Cox", "Ward", "Flores",
    "Alexander", "Hughes", "Washington", "Butler", "Simmons", "Foster", "Bryant", "Vasquez", "James", "Alexander",
    "Jordan", "Hamilton", "Graham", "Douglas", "Woods", "Coleman", "Stone", "Bennett", "Fisher", "Caldwell",
    "Curtis", "Snyder", "Dixon", "Howard", "Ramos", "Perez", "Sullivan", "Price", "Bishop", "Gibson",
    "Berg", "Meyer", "Webb", "Davidson", "Williamson", "Murray", "Ford", "Webster", "Walsh", "Hunter",
    "Fox", "Harrison", "Chavez", "Chang", "Ng", "Fleming", "Schmidt", "Shaw", "Freeman", "Hansen",
    "Kim", "Bishop", "Bowers", "Tucker", "Burns", "Henderson", "Curtis", "Larson", "Barnes", "Henry",
    "Gentry", "Mendez", "Jenkins", "Patel", "Hodges", "Hicks", "Walters", "Lynch", "Harrison", "Arnold"
]
def random_email():
    account = ''
    randomlength = 5
    base_str = 'qwertyuioplkjhgfdsazxcvbnm0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        account += base_str[random.randint(0, length)]
    logger.info(account)
    return account
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
# 创建页面对象
co = ChromiumOptions().auto_port()  # 指定程序每次使用空闲的端口和临时用户文件夹创建浏览器
co.headless(True)   # 无头模式
co.set_argument('--no-sandbox')  # 无沙盒模式
co.set_argument('--headless=new')  # 无界面系统添加
co.set_paths(browser_path="/opt/google/chrome/google-chrome")  # 设置浏览器路径
co.set_argument('--disable-gpu')    # 禁用gpu，提高加载速度
co.set_user_agent("Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:65.0) Gecko/20100101 Firefox/65.0") 
co.incognito(True)
co.remove_extensions()
browser = ChromiumPage(co)
tab = browser.latest_tab
logger.info('打开 url')


tab = browser.latest_tab
for i_cishu in range(10):
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
    ele = tab.ele('css=#id_first_name')
    ran = random.randint(2, 97)
    ele.input(firstnames[ran])
    logger.info(firstnames[ran])

    ele = tab.ele('css=#id_last_name')
    ran = random.randint(2, 97)
    ele.input(lastnames[ran])
    logger.info(lastnames[ran])

    firstname = random_email()
    ele = tab.ele('css=#id_username')
    username = lastnames[i_cishu] + firstname
    ele.input(username)

    ele = tab.ele('css=#id_email')
    ele.input('cornerluossj@gmail.com')

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
    ele = tab.ele('css=#id_question')
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
        #anpush_payload['content'] = ele.text
        #response = requests.post(anpush_url, headers=anpush_headers, data=anpush_payload)
        exit()



