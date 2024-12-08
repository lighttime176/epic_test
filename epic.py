
from DrissionPage import ChromiumPage
from DrissionPage import ChromiumOptions
import time,logging
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
cookies = {
  "EPIC_DEVICE": "82d888996028413cb5c389f72ab2f701",
  "_epicSID": "bb6afc3973fd403fae4111167935f0fd",
  "EPIC_LOCALE_COOKIE": "zh-CN",
  "cf_clearance": "DYPKU5YXz4BH56jG_aohJ89WmxHLdUfEuWLnHRzvfAQ-1733623168-1.2.1.1-e0Fk_LFYbG6WR4A90.Hh4U0s8vcV7nvSKMxWHkTyT3IIBTPx0ONZvlJvZHU7_7EZMtvw9ryk0kO_icW1rRKOEo5Hvp.KljLxgUydW_XcbFI9LdipzJsaokB3oE31pD292eIYaHWs.Eea4OK8ooZdO6aDu2ZX13r8uNTBsmOYC4LKzaSS_rzT_0DLY8lznC.uqc5QK_9zUcVXjU4FAbd4NIdRaD5mI6MsJPVMx249KH36iquJYngfsKkItL6tlgd2RaitTKsWGplGbqIIyZUs2RmI2Y7OjUJ1ubcv632MH3N8UcQf5LZny2cJmmieVVAqSvZT5G9sodbJGiB5hgL_4fouYiZTF.Hj2Ylojd1Rxr8UOXp.wIXE1sOm4bQ7U7LRd3UH42eouj47dJrFgKMHTw",
  "_tald": "f8c185da-ab39-48e8-9ebc-ce9f20b19432",
  "EPIC_SSO": "3178dc583f714e78b5e7186bfa6a0cdc",
  "EPIC_BEARER_TOKEN": "4097f99e047b40788e92308c468ca29f",
  "EPIC_SSO_RM": "3178dc583f714e78b5e7186bfa6a0cdc",
  "EPIC_EG1": "eg1~eyJraWQiOiJnX19WS2pTU21xSjB4WmoxUllrTEdLUTdkbkhpTTlNTGhGVndLUHlTREI0IiwiYWxnIjoiUFMyNTYifQ.eyJhcHAiOiJkaWVzZWx3ZWIiLCJzdWIiOiI5YzlmZGI0NTNhYWQ0Nzk3ODNjYjEzMjBjMDlkZjdkMyIsImR2aWQiOiI4MmQ4ODg5OTYwMjg0MTNjYjVjMzg5ZjcyYWIyZjcwMSIsIm12ZXIiOmZhbHNlLCJjbGlkIjoiODc1YTNiNTdkM2E2NDBhNmI3ZjliNGU4ODM0NjNhYjQiLCJkbiI6ImJhaXBwcGhoaCIsImFtIjoidG9rZW5fdG9fdG9rZW4iLCJwIjoiZU5xbFZ0RnUyekFNL0o4aEJacW1YUmNEK1lBQmZScjJBN1JFSjBSa1NaQmt0OW5YajVJdHgwNlQyZWxlRXN1U2FPcnVlSlIxUmpZaUZMWXBGWW5DZGtPL2Uxb1p0d2ROZnlDUTBRWEltdmhYQ05Qb1VHekZ0cExsODhzR1FENi9ibDkvYkVTNTNqdzlpc2V0ckY3bHBoanZqYkVjdG9UditTTU9yWEdoQ09EMkdIYnJsVEIxM1dnUzNmS0NkRUNuUWZFNmtJWEhFRWp2WTVTTGRmalJyOHRweFdoUHF6enFQNWFIMzNnS0d3WEJnVGh5d0hNeTNuSTBuRDBVSjZxb2RPQk9lU3NGckR1a0pEcEdUcUQzeHVYWldaQThLUFMvRWhZY3BGUkdITi9JaHdXSlBLOVFCd29LYS83dmdMSGdHUkdHYWIzeVRlbUZJNXVJVzVxTVVFRDFRNGthS3dvM2dvemZQVWlzK010MktoOFBXcGJtQXlNcUYyRE5aMkNVUWhGajc5WXYvN0U3MGJKYnI2ZHMrd000bEFQYkJ3YmF1Tk5JTHYyL24vOVVqUUVrQkVpU3FoeWhsbjRCYVM4ckZpNG9NK1JpcWdwZFJLbzJjZ0R3clBackRCUWtFL09ubjNMQ1JvTGJoK1ZvQVd1T0licGVLN3Z2NDVUNE1XWmpCS1ZTQzlUeTkvdkp5NXJxVDhadjBBZllPendybEVzRUpkYmRjUVkySksvWTNjKzJWWEFLVkdNQlN0MUJBalAybVlaa0RPZHlXbTV5bzAySkwzUXRDU1ROSjljQzc2WGtuZndoYnVqRWY4ZkdZTUJIeWk0Z1hsNDRUYXlJb21LeWRwdWJIaXZZakFObWZiSkJUQzFkMFJFNWgrdDJZTkhWNUgyblV3dW5CUE5pWEpqaTVPc1NXMVRHUnFlbEZzUnBxSlg1Mm91Sk1UV285NlJ4VW41Rm1vZzFDTzZJZ1hVbGNMRDN5S1JTdm5pakZ2L1Jmc1p0NnJQVWwvTWdrMjFlNEpPSHMvdWhDUWNCTmxvM094dEs4c0swZUs2cFlDeUo1TXZRYUhIZ28rZWl5MjNNTms0Y2dEdmhZRXpEMHM5VFpVTktrcTVNa1o1cWJ2Y1YxL3pOTnN2NXhLSWRQR0dlTkU2SVBYM0FnWjg3Z1ZXa2NIUmRpVU9lY1BnT1RpNUd1MXYra0UzL0MrMHFXOUFOcDU3di9sUDd6bXJLNXRTSDJVT05mdHpoVGV6d1grOVpNZFRVL2pMN0YrZG42UWY4Ylk2bzAyTVRsMVNOWXJUVldKNVJ0WnpRbGZKS3R4c3UyV1QvbHZ1TlJoZHZkbnZYM1NpYkNPQ1MwcTFaeTlDYmE3emhSSFdQampFRjZpL1EzTVgrIiwiaWFpIjoiOWM5ZmRiNDUzYWFkNDc5NzgzY2IxMzIwYzA5ZGY3ZDMiLCJzZWMiOjAsImFjciI6InVybjplcGljOmxvYTphYWwyIiwiY2xzdmMiOiJkaWVzZWx3ZWIiLCJscHYiOjE3MzM2MjMyMDEsInQiOiJzIiwiYXV0aF90aW1lIjoxNzMzNjIzMjAxLCJpYyI6dHJ1ZSwiZXhwIjoxNzMzNjUyMDAyLCJpYXQiOjE3MzM2MjMyMDYsImp0aSI6IjJjOTM3YmY2N2M2MTQ3YTU5MDNiMGNjZDcyZmIyYmI3In0.zaA-dWn7NZCvQaQ7aeKhUXU1133UKvSh7AqmIJS5-t7eKZzpPHB9ECN_IMZM_41SrKJiofwmDUyJlRHwvLd9Z06KKKSm1XkaT1zxlUDpTn7KYdl02QNMcl9d_a3bNq7QP-_G_mVhNqkV095uNjIzL9ngOUVpatarbD3ZgHQVXi8PBntAqkBDSA0uIaeJyR0vVxELblDxlR-4-SWxWRmKdaR9P200mUlryalorAtIcKRVkRrOgiQT-x9wjZM1mxnBJ0M-ui9Z9npmXqWV4_aVvcuxoT4REaGrE9-f6Z8ZkqXp2u3DnQoJDaFaIfuqOyJ4p9590tLa4PnaDU0_GDhR7vtKHm7vu1IatO2tB4VMDf83bKNb29dcvJUhj93Pxkachn8eA45ofP4Ky5_ekllNh9SXy0bbN7QGF8shO79RrbuG9qz2IEfuCtV2AyARG6GqWaFtX0Jxg5qWXl28xoclYE-wJVTHwsX9crLodjeaixBlsETf_V8KWT3Y1cqke8W14KsjLJlC9s-yVR_gCFhSa2apKbKD-RyDxSOk-u1O7wlbBQU2ohfv_OJRyAGkuk6oufTcLWeswnEA6BQKZ9bKxdqPxmfmN2yvxYAvnOZyWBujBfhcsUcE7l9MSKb0eV2gAK-8VIUBfa09znOL1aEatR62dLWXYdU9x8y_ZZ8RyN0",
  "REFRESH_EPIC_EG1": "eg1~eyJraWQiOiJnX19WS2pTU21xSjB4WmoxUllrTEdLUTdkbkhpTTlNTGhGVndLUHlTREI0IiwiYWxnIjoiUFMyNTYifQ.eyJzdWIiOiI5YzlmZGI0NTNhYWQ0Nzk3ODNjYjEzMjBjMDlkZjdkMyIsImR2aWQiOiI4MmQ4ODg5OTYwMjg0MTNjYjVjMzg5ZjcyYWIyZjcwMSIsInQiOiJyIiwiY2xpZCI6Ijg3NWEzYjU3ZDNhNjQwYTZiN2Y5YjRlODgzNDYzYWI0IiwiZXhwIjoxNzMzNzM4NDA2LCJhbSI6InRva2VuX3RvX3Rva2VuIiwianRpIjoiODE2NDg1ZjVmOGUwNDE4MzkyYmEwNWU0N2YwNTk0YTcifQ.v9xouJZ-Wh7B99dOFX5Q4rNpYImV_DNFKZ8zgJattRYq7Le2xGoxkBdGFAkILURsLXCqRJwk590XnRchJ3yc73OgsanGiFOtJFUhdEipwsIzYQqBunaqNKZK0wDti5HBlDKzfWnEZwS6nPssgr0lSTeJmNsM8YLl2FLgBNYqp1rqunqlHQtA-2y-jUEN4S7tTcxcrqS0uFDfz2y_kxglMz9DdrheQGIupIsOso6hmMyMY42VM8ycUdNGfgbHFhzcgKFZsiRwTNuUhBU0P-R_KXw5abJfOSiqWbEyug34ttkTu7WrakgiLBy21WWr09IqjZ5f7CXpvCXZ6B8NdyAcPJnQN2l7vhZYOSh1TJeJgWJZ8XheQnuiu2I5-5EC-b0bEv4EJ98JH7Dpj7hiMv67V6CrsbwJS4WA4vv1RTjl3YO8PCB7QAsxNqOaan92KLRfMfKoTTrwxW78uCNxAf-ZemH1qJl790Juhsn28GQDIu3BQ6Vs-tN8qoeBLQBTW6JbXj99aGc4Z1BnaAOr-Atm_BVrffb0fQnzqIxBbx63nmRtkbP12eGfAbvq1Omb_hh4TQNZew5M2S-6JkHqzUmT7aUNBZEnBrdbs7LVMSdNzZ8ChT9IGM4oxXbUudJUxqEaZSikjMs5e0asSlmmzyilbRhnMpGV5QIWz3tTeaXhI2M",
  "refreshTokenExpires": "2024-12-09T10%3A00%3A06.009Z",
  "storeTokenExpires": "2024-12-08T10%3A00%3A02.008Z",
  "__cf_bm": "Ijx2oIJFX8JqgVkm_CmpkJIqhsPh8pW1ooyeHHtPynU-1733623225-1.0.1.1-ik5Z.G0SBQwfij8fcydC7.wX7l5z5EjRv_5UahKOou3CUjCXpyP7BH2QTQ_Z9sRm0QWmG6v1kKKKHpoRxUbnPQ",
  'domain': 'store.epicgames.com'
}
logger = logging_init()
# 连接浏览器
co = ChromiumOptions().auto_port()  # 指定程序每次使用空闲的端口和临时用户文件夹创建浏览器


browser = ChromiumPage(co)

tab = browser.latest_tab
tab.set.cookies(cookies)
# tab.set.window.full()
# 访问网页
tab.get('https://store.epicgames.com/zh-CN/p/bus-simulator-21')
time.sleep(1)


ele = tab.ele('css=#dieselReactWrapper > div > div > div.css-1vplx76 > main > div.css-1dnikhe > div > div > div > div.css-j7qwjs > div:nth-child(4) > div > aside > div > div > div.css-bco1gb > div:nth-child(1) > button')
ele.click()
print(ele)
time.sleep(1)
with open(r"./test_browser.html", "w", encoding="utf-8") as f:
    f.write(tab.html)
tab.get_screenshot(path=r"./test_browser_page.png", full_page=False)
# ele = tab.ele('text:下订单')
# print(ele.text)
# ele.click()
# print(eles)
# print(type(eles))
# for i_ele in eles:
#   print('1')
#   result = i_ele.text.find('截止')
#   if result != -1:
#     print(i_ele.text)
    # i_ele.click()



# input('sss')
# browser.quit()
