from five import grok

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Item

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable

from infoporto.community import MessageFactory as _
from plone.supermodel import model

from plone.namedfile import field as namedfile

from plone import api

class IMarketItem(model.Schema):

    contact_name = schema.TextLine(
        title=_(u'Contact Name'),
    )

    item_city = schema.TextLine(
        title=_(u'Item City'),
        required=False,
    )

    contact_phone = schema.TextLine(
        title=_(u'Contact Phone'),
        required=False,
    )

    contact_email = schema.TextLine(
        title=_(u'Contact E-mail'),
        required=True,
    )

    picture = namedfile.NamedBlobImage(
        title=_(u"Picture"),
        required=False,
    )


# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class MarketItem(Item):
    grok.implements(IMarketItem)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# market_item_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    """ sample view class """

    grok.context(IMarketItem)
    grok.require('zope2.View')

    grok.name('view')

    def __call__(self):
        if 'form.buttons.comment' in self.request:
            self.request_info()
            return self.request.response.redirect(self.context.absolute_url())

        return super(View, self).__call__()

    def request_info(self):
        sender = self.request.form['sender']
        body = self.request.form['body']

        if sender == "" or body == "":
            print 'Missing required fields'
            return

        api.portal.send_email(
            recipient=self.context.contact_email,
            sender=sender,
            subject=self.context.title,
            body=body,
        )

    

    # Add view methods here
