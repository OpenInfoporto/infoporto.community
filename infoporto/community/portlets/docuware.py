from zope.interface import Interface
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider
import hashlib
from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.i18nmessageid import MessageFactory
from plone import api


__ = MessageFactory("plone")


class IDocuware(IPortletDataProvider):
    pass


class Assignment(base.Assignment):
    implements(IDocuware)

    def __init__(self):
        pass

    @property
    def title(self):
        return __(u"IDocuware")


class Renderer(base.Renderer):
    def getCurrentUser(self):
        return api.user.get_current()

    def completepath(self):
        HOST = 'http://10.5.6.184:8080/contship/documenti.php?user=%s&key=%s'
        SECRET = '_1234'

        user = api.user.get_current()
        username = user.getMemberId()

        hashed = hashlib.md5("%s%s" % (username, SECRET)).hexdigest()

        return HOST % (username, hashed)

    render = ViewPageTemplateFile('docuware.pt')


class AddForm(base.AddForm):
    form_fields = form.Fields(IDocuware)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(IDocuware)
