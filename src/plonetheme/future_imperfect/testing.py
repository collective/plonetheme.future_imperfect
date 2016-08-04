# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plonetheme.future_imperfect


class PlonethemeFutureImperfectLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=plonetheme.future_imperfect)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plonetheme.future_imperfect:default')


PLONETHEME_FUTURE_IMPERFECT_FIXTURE = PlonethemeFutureImperfectLayer()


PLONETHEME_FUTURE_IMPERFECT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLONETHEME_FUTURE_IMPERFECT_FIXTURE,),
    name='PlonethemeFutureImperfectLayer:IntegrationTesting'
)


PLONETHEME_FUTURE_IMPERFECT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLONETHEME_FUTURE_IMPERFECT_FIXTURE,),
    name='PlonethemeFutureImperfectLayer:FunctionalTesting'
)


PLONETHEME_FUTURE_IMPERFECT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLONETHEME_FUTURE_IMPERFECT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlonethemeFutureImperfectLayer:AcceptanceTesting'
)
