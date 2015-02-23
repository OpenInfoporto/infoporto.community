from zope.interface import Interface
from zope.interface import implements

from plone.app.portlets.portlets import base
from plone.portlets.interfaces import IPortletDataProvider

from zope import schema
from zope.formlib import form
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from zope.i18nmessageid import MessageFactory
from plone import api


__ = MessageFactory("plone")


class IchangeTurn(IPortletDataProvider):
    pass


class Assignment(base.Assignment):
    implements(IchangeTurn)

    def __init__(self):
        pass

    @property
    def title(self):
        return __(u"IchangeTurn")


class Renderer(base.Renderer):
    def getCurrentUser(self):
        return api.user.get_current()

    render = ViewPageTemplateFile('changeTurn.pt')


class AddForm(base.AddForm):
    form_fields = form.Fields(IchangeTurn)

    def create(self, data):
        return Assignment(**data)


class EditForm(base.EditForm):
    form_fields = form.Fields(IchangeTurn)
