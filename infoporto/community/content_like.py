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

from datetime import datetime
# Interface class; used to define content-type schema.

class IContentLike(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """

    creation_date = schema.Datetime(
            title=_(u"Creation Date"),
            default=datetime.now()
        )

    uuid = schema.TextLine(
            title=_(u"Content"),
        )

class ContentLike(Item):
    grok.implements(IContentLike)

    # Add your class methods and properties here
    pass



class SampleView(grok.View):
    """ sample view class """

    grok.context(IContentLike)
    grok.require('zope2.View')

    # grok.name('view')

    # Add view methods here
