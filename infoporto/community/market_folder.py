from five import grok

from Products.CMFCore.utils import getToolByName

from z3c.form import group, field
from zope import schema
from zope.interface import invariant, Invalid
from zope.schema.interfaces import IContextSourceBinder
from zope.schema.vocabulary import SimpleVocabulary, SimpleTerm

from plone.dexterity.content import Container

from plone.directives import dexterity, form
from plone.app.textfield import RichText
from plone.namedfile.field import NamedImage, NamedFile
from plone.namedfile.field import NamedBlobImage, NamedBlobFile
from plone.namedfile.interfaces import IImageScaleTraversable


from infoporto.community import MessageFactory as _


# Interface class; used to define content-type schema.

class IMarketFolder(form.Schema, IImageScaleTraversable):
    """
    Description of the Example Type
    """

    # If you want a schema-defined interface, delete the model.load
    # line below and delete the matching file in the models sub-directory.
    # If you want a model-based interface, edit
    # models/market_folder.xml to define the content type.



# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class MarketFolder(Container):
    grok.implements(IMarketFolder)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# market_folder_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.

class View(grok.View):
    """ sample view class """

    grok.context(IMarketFolder)
    grok.require('zope2.View')

    grok.name('view')

    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def getItems(self):
        results = self.catalog(path=dict(query='/'.join(self.context.getPhysicalPath()), depth=1), sort_on='getObjPositionInParent')
        return [ r.getObject() for r in results ]
