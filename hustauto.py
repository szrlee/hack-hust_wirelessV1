import urllib 
import urllib2 
import string

def post(url, data): 
    req = urllib2.Request(url) 
    data = urllib.urlencode(data) 
    #enable cookie 
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor()) 
    response = opener.open(req, data) 
    return response.read() 
def encrypt(password){
    str = password
#    temp = new Array(password.length);
#    for i in range(0,len(password))
#        temp[i] = str.charCodeAt(i)^0xff
#        ret += String.fromCharCode(temp[i]);
    return ret;

def main(): 
    posturl = "http://192.168.50.2:8080/portal/hust/desk/onlogin.jsp"
    username = raw_input（'username'）
    password = raw_input('password')
    data={'userName='+username+'&userPwd='+ret}
    print post(posturl, data) 
                       
if __name__ == '__main__': 
    main()  
