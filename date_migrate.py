from app.models import User, Item

from app import db

import datetime

from dateutil import parser

# users = db.session.query(User).all()
# for each in users:
#     if each.joined:
#         each.joined = datetime.datetime.strptime(each.joined, '%Y/%m/%d %H:%M:%S')


items = db.session.query(Item).all()
# for each in items:
#     print each.opened_at.date()


for each in items:
    if each.opened_at:
        each.opened_at = parser.parse(each.opened_at)
        db.session.add(each.opened_at)
        print type(each.opened_at)

    if each.resolved_at:
        # each.resolved_at = parser.parse(each.resolved_at)
        # db.session.add(each)
        print type(each.resolved_at)

db.session.commit()
print "Done!"