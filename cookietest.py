import requests
jar = requests.cookies.RequestsCookieJar()
jar.set('Hm_lvt_4ab5ca5f7f036f4a4747f1836fffe6f2', '1603174636', domain='.hifini.com', path='/')
jar.set('bbs_token', 'HutOfjOUPTnUvskveYPKnHLH6_2BskyeH1M3q_2F_2BFZPQPzuSAEPxSLNDdu8oJ80_2FJ3I_2Frfo23KNB85kpplQb7BBHcdkUqA_3D', domain='.hifini.com', path='/')
jar.set('bbs_sid', 'jq2vgg7dejacs5sihug10ni3d5', domain='.hifini.com', path='/')
url = 'https://www.hifini.com/sg_sign.htm'
r = requests.post(url, cookies=jar)
print(r.text)
