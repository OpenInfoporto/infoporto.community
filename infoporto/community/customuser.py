# should be moved to different file
from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api


class firstLogin():
    template = ViewPageTemplateFile('templates/customuser.pt')

    def __call__(self):
        return self.template()
