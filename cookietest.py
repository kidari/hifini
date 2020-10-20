import requests,os
jar = requests.cookies.RequestsCookieJar()
jar.set('Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2', os.environ["Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2"], domain='.hifini.com', path='/')
jar.set('bbs_token', os.environ["bbs_token"], domain='.hifini.com', path='/')
jar.set('bbs_sid', os.environ["bbs_sid"], domain='.hifini.com', path='/')
url = 'https://www.hifini.com/sg_sign.htm'
r = requests.post(url, cookies=jar)
print('HIFI打卡完毕')
