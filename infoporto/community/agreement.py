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

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class agreement(Item):
    grok.implements(Iagreement)

    # Add your class methods and properties here
    pass


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
