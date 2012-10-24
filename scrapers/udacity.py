import urllib2
import json
from BeautifulSoup import BeautifulSoup

url = "http://www.udacity.com/courses"
request = urllib2.Request(url)
response = urllib2.urlopen(request)

the_page = response.read()
for l in the_page.split("\n"):
   if l[0:len("PRELOADED_COURSES")] == "PRELOADED_COURSES":
      data = json.loads(l[len("PRELOADED_COURSES = "):])

courses = []
for c in data["courses"]:
   course = {}
   course['name'] = "%s: %s"%(c['title'],c['name'])
   course['service'] = 'u'
   course['course_id'] = "%s"%(c['course_id'])
   professors = []
   for p in c['instructors']:
      professors.append(p['name'])
   course['professor'] = "%s"%(", ".join(professors))
   course['url'] = "http://www.udacity.com/overview/%s"%(c['path'])
   courses.append(course)
print json.dumps(courses)