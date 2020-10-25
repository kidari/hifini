# -*- coding: utf-8 -*-
import requests,os,time
jar = requests.cookies.RequestsCookieJar()
jar.set('Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2', os.environ["Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2"], domain='.hifini.com', path='/')
jar.set('bbs_token', os.environ["bbs_token"], domain='.hifini.com', path='/')
jar.set('bbs_sid', os.environ["bbs_sid"], domain='.hifini.com', path='/')
url = 'https://www.hifini.com/sg_sign.htm'
r = requests.post(url, cookies=jar, headers={"Content-type": "text/html; charset=utf-8"})
resultHtml = r.text
def contextStr(str='==='):
  context={
      "msg_type": "text",
      "content": {
          "text": str+"hifi "+time.strftime('%H:%M:%S', time.localtime(time.time()+28800))
      }
  } 
  return context
roburl = os.environ["MSG_ROB"]
if "成功签到" in resultHtml:
  resultStr = contextStr("成功签到")
  res=requests.post(url=roburl,data=protect(json.dumps(resultStr)),headers={"Content-type": "application/json; charset=utf-8"})
if "已经签过" in resultHtml:
  resultStr = contextStr("已经签过")
  res=requests.post(url=roburl,data=protect(json.dumps(resultStr)),headers={"Content-type": "application/json; charset=utf-8"})  
else:
  resultStr = contextStr("签到失败")
  res=requests.post(url=roburl,data=protect(json.dumps(resultStr)),headers={"Content-type": "application/json; charset=utf-8"})
