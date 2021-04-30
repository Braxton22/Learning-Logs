import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()

t = Topic.objects.get(id=1)

entries = t.entry_set.all()

for entry in entries:
    print(entry)

'''
for t in topics:
    print(f"Topic ID: {t.id}   Topic: {t}")

entries = Entry.objects.all()

for x in entries:
    print(f"Topic: {x.topic}")
    print(f"Text: {x}")
    print(f"Date Added: {x.date_added}")
'''