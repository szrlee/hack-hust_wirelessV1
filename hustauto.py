import urllib 
import urllib2 
import base64
def post(url,data): 
    req = urllib2.Request(url) 
    data = urllib.urlencode(data) 
    #enable cookie 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
    response = opener.open(req,data) 
    return response.read() 

def main(): 
    posturl = "http://192.168.50.2:8080/portal/hust/desk/onlogin.jsp"
    username = raw_input('username')
    password = raw_input('password')
    ret = base64.encodestring(password)
    data={'userName='+username+'&userPwd='+ret}
    print ret
    print post(posturl,data) 
                       
if __name__ == '__main__': 
    main()  
