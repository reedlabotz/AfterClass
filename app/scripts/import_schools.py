import sys,os
sys.path.append(os.path.abspath('..'))

from django.core.management import setup_environ 
import settings 
setup_environ(settings)

import json
from app.social.models import Course

json_file = sys.argv[1]

json_data=open(json_file)

data = json.load(json_data)
for course in data:
   c = Course(**course)
   c.save()
   print c
