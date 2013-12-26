import urllib 
import httplib
import base64
username = raw_input('username:')
password = raw_input('password:')
try:
    ret = base64.encodestring(password)
    data = {'userName':username,'userPwd':ret}
    posturl = "http://192.168.50.2:8080/portal/hust/desk/onlogin.jsp"
    params = urllib.urlencode(data)
    headers = {'Content-Type':'application/x-www-form-urlencoded',
            'Accept':'text/html,application/xhtml+xml,application/xml',
            'Accept-Encoding':'gzip,deflate',
            'Accept-Language':'zh-cn',
            'Connection':'keep-alive',
            'Host':'192.168.50.2:8080',
            'Referer':'http://192.168.50.2:8080/portal/hust/desk/index.jsp',
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64; rv:26.0) Gecko/20100101 Firefox/26.0'}
    httpClient = httplib.HTTPConnection('192.168.50.2:8080')
    httpClient.request(method="POST",url=posturl,body=params,headers=headers)
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
    print response.getheaders() 
except Exception, e:
    print e
httpClient.close()
                       
