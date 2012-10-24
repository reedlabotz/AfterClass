import urllib
import urllib2
import string
import sys
import json
from BeautifulSoup import BeautifulSoup

url = 'https://www.edx.org/courses'

request = urllib2.Request(url)
response = urllib2.urlopen(request)

the_page = response.read()
pool = BeautifulSoup(the_page)

results = pool.findAll('article',{'class':'course'})
courses = []
for r in results:
   num = r.findAll('span',{'class':'course-number'})[0].getText()
   name = r.findAll('h2')[0].getText()
   name = name.split(num)[1]
   course = {}
   course['name'] = name
   course['course_id'] = num
   course['service'] = 'e'
   courses.append(course)
print json.dumps(courses)