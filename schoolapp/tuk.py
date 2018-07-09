
import requests
import sys
import HTMLParser
import subprocess
from bs4 import BeautifulSoup

import json
import sys
# from .views import classstudent

reload(sys)
sys.setdefaultencoding("utf-8")
# fire2=firebase.FirebaseApplication("https://requestv2.firebaseio.com",None)




grad = 'http://ar.tukenya.ac.ke/img/Graduate-form.pdf'
invoice = 'http://ar.tukenya.ac.ke/includes/invoice4.php'


class SchoolSite:
    def feestatement(self, id, print_name, stdno):
        # url='http://ar.tukenya.ac.ke/checklogin.php?action=login'
        # reg=stdno
        # r=requests.post(url,{'PersistentCookie':'yes','username':reg})
        # soup=BeautifulSoup(r.content,'html.parser')
        soup = ""
        name = ""
        with requests.session() as c:
            url = 'http://ar.tukenya.ac.ke/checklogin.php?action=login'
            c.post(url, {'PersistentCookie': 'yes', 'username': stdno})
            pg = c.post("http://ar.tukenya.ac.ke/summary.php", {"common_units_skip": "SKIP INTERVIEW"})
            soup = BeautifulSoup(pg.content, 'html.parser')
            names = soup.find_all('h1')[0].text
            data = []
            table = soup.find_all('table')[1]

            rows = table.find_all('tr')
            for row in rows:
                cols = row.find_all('td')
                cols = [ele.text.strip() for ele in cols]
                data.append([ele for ele in cols if ele])

            name =names
            reg = stdno
            Print_id = print_name
            id = id
            semester = data[8][1]
            course_code = data[3][1]
            course_name = data[4][1]
            balance = data[9][1]
            bal = float(balance)
            if bal <= 0:
                message ='Eligible To Sit For This Paper'
                cl= 0
            else:
                message = 'Not Eligible TO Sit For This Paper'
                cl=1

            details = {'name': name, 'Reg_no': reg, 'semester': semester, 'course_code': course_code, 'cl':cl,
                       'course_name': course_name, 'bal': bal, 'print_id': Print_id, 'id': id, 'message': message}
            # detail= classstudent()
            # detail.student(name)

            # print details
            # print name
            # print reg
            # print semester
            # print course_code
            # print course_name
            # print bal


        return  details
