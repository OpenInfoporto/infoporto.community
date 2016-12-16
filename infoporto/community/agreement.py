from five import grok

from z3c.form import group, field
from zope import schema

from plone.dexterity.content import Item

from plone.directives import form

from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from infoporto.community import MessageFactory as _

from Products.Five import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone import api

import json

# Interface class; used to define content-type schema.

class Iagreement(form.Schema, IImageScaleTraversable):
    """
    Description of the Agreement Type
    """

    start = schema.Datetime(
            title=_(u"Start date"),
            required=False,
        )

    end = schema.Datetime(
            title=_(u"End date"),
            required=False,
        )

    details = RichText(
            title=_(u"Details"),
            description=_(u"Details about the agreement"),
            required=False,
        )

    icon = NamedImage(
			title=_(u"Icon"),
			description=_(u"Used in some views"),
			required=False,
		)

    contact_name = schema.TextLine(
            title=_(u"Contact name"),
            required=False,
        )

    contact_email = schema.TextLine(
            title=_(u"Contact e-mail"),
            required=False,
        )

    contact_phone = schema.TextLine(
            title=_(u"Contact phone"),
            required=False,
        )
    
    contact_address = schema.TextLine(
            title=_(u"Contact address"),
            required=False,
        )


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class agreement(Item):
    grok.implements(Iagreement)

    # Add your class methods and properties here
    def getLikes(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        documents = catalog(portal_type='infoporto.community.contentlike')
        likes = []
        for dd in documents:
            if dd.getObject().uuid == api.content.get_uuid(obj=self):
                likes.append(dd.getObject())

        return len(likes)


# View class
# The view will automatically use a similarly named template in
# agreement_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    """ sample view class """

    grok.context(Iagreement)
    grok.require('zope2.View')

    grok.name('view')

    # Add view methods here


class ContactSupplier(BrowserView):
    template = ViewPageTemplateFile('agreement_templates/contact_supplier.pt')

    def getCurrentName(self):
        current = api.user.get_current()
        return current.getUserName()

    def __call__(self):
        if self.request.get('action') == 'send':
            #TODO: implement msg send
            pass

        return self.template()


class showLikes(BrowserView):
    template = ViewPageTemplateFile('agreement_templates/show_likes.pt')

    def getItems(self):
        catalog = api.portal.get_tool(name='portal_catalog')
        documents = catalog(portal_type='infoporto.community.agreement')
        return [el.getObject() for el in documents]


    def __call__(self):
        return self.template()

class likeMobileIt(BrowserView):
    
    def __call__(self):
        body = self.request.get('BODY')
        body = json.loads(body)
        uuid = body.get('uuid')

        portal = api.portal.get()
        obj = api.content.create(
            type='infoporto.community.contentlike',
            title='Like from %s for %s' % (api.user.get_current(), uuid),
            uuid=uuid,
            container=api.content.get(path='/servizio/likes/'))

class likeIt(BrowserView):
    def __call__(self):
        portal = api.portal.get()
        obj = api.content.create(
            type='infoporto.community.contentlike',
            title='Like from %s for %s' % (api.user.get_current(), self.request.uuid),
            uuid=self.request.uuid,
            container=api.content.get(path='/servizio/likes/'))
        return "Grazie!"
