from __future__ import unicode_literals
from redminelib import Redmine

REDMINE_URL = 'http://163.172.204.245:8002'
REDMINE_KEY = 'a237575c6ab6b747e2d5c069d1d4c699d8f56ea9'
# REDMINE_KEY = '2191d4d6f6bfb37e14002af1ac10a4218e1e8c0f'

redmine = Redmine(REDMINE_URL, key=REDMINE_KEY)
print "\n\n\n",redmine,"\n\n"

user = redmine.user.create(
	login='poojasom',
	password='poojasom@123',
	firstname='pooja',
	lastname='som',
	mail='pysomvanshi@gmail.com'
)

print user

# allusers = redmine.user.all()
# user_out = dir(allusers)
# print user_out