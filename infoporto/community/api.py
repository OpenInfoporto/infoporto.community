"""
Basic API for misc contents

"""
from plone import api
import json


def getByType(ctype):
    catalog = api.portal.get_tool(name='portal_catalog')
    return catalog(portal_type=ctype)
    

class getNews():
    def __call__(self):
        res = []
        for el in getByType('News Item'):
            o = el.getObject()
            rel = dict(uid=o.UID(), title=o.title, description=o.Description(),
                       text=o.getText(),
                       modification_date=o.modification_date.strftime('%d-%m-%Y %H:%M:%S'))
            res.append(rel)

        return json.dumps(res)

class getAgreements():
    def __call__(self):
        res = []
        for el in getByType('infoporto.community.agreement'):
            o = el.getObject()
            rel = dict(uid=o.UID(), title=o.title, description=o.Description(),
                       modification_date=o.modification_date.strftime('%d-%m-%Y %H:%M:%S'),
                       contact_email=o.contact_email, contact_name=o.contact_name, 
                       contact_phone=o.contact_phone, 
                       start=o.start.strftime('%d-%m-%Y %H:%M:%S'), 
                       end=o.end.strftime('%d-%m-%Y %H:%M:%S'))
            res.append(rel)

        return json.dumps(res)

class getEvents():
    def __call__(self):
        res = []
        for el in getByType('Event'):
            o = el.getObject()
            rel = dict(uid=o.UID(), title=o.title, description=o.Description(),
                       modification_date=o.modification_date.strftime('%d-%m-%Y %H:%M:%S'),
                       contact_name=o.contactName,
                       contact_email=o.contactEmail,
                       contact_phone=o.contactPhone,
                       event_url=o.eventUrl,
                       start_date=o.startDate.strftime('%d-%m-%Y %H:%M:%S'),
                       end_date=o.endDate.strftime('%d-%m-%Y %H:%M:%S'),
                        )
            res.append(rel)

        return json.dumps(res)

