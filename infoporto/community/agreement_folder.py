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

from plone.supermodel import model

from infoporto.community import MessageFactory as _


class IAgreementFolder(model.Schema):


    title = schema.TextLine(
        title=_(u'Folder Name'),
    )

# Custom content-type class; objects created for this content type will
# be instances of this class. Use this class to add content-type specific
# methods and properties. Put methods that are mainly useful for rendering
# in separate view classes.

class AgreementFolder(Container):
    grok.implements(IAgreementFolder)

    # Add your class methods and properties here
    pass


# View class
# The view will automatically use a similarly named template in
# agreement_folder_templates.
# Template filenames should be all lower case.
# The view will render when you request a content object with this
# interface with "/@@sampleview" appended.
# You may make this the default view for content objects
# of this type by uncommenting the grok.name line below or by
# changing the view class name and template filename to View / view.pt.


class View(grok.View):
    """ sample view class """

    grok.context(IAgreementFolder)
    grok.require('zope2.View')

    grok.name('view')

    @property
    def catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    def getAgreements(self):
        results = self.catalog(portal_type='infoporto.community.agreement', path=dict(query='/'.join(self.context.getPhysicalPath()), depth=3), sort_on='getObjPositionInParent')
        
        return [ r.getObject() for r in results ]
