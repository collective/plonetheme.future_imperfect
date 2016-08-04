# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plonetheme.future_imperfect.testing import PLONETHEME_FUTURE_IMPERFECT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that plonetheme.future_imperfect is properly installed."""

    layer = PLONETHEME_FUTURE_IMPERFECT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plonetheme.future_imperfect is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'plonetheme.future_imperfect'))

    def test_browserlayer(self):
        """Test that IPlonethemeFutureImperfectLayer is registered."""
        from plonetheme.future_imperfect.interfaces import (
            IPlonethemeFutureImperfectLayer)
        from plone.browserlayer import utils
        self.assertIn(IPlonethemeFutureImperfectLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLONETHEME_FUTURE_IMPERFECT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plonetheme.future_imperfect'])

    def test_product_uninstalled(self):
        """Test if plonetheme.future_imperfect is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'plonetheme.future_imperfect'))

    def test_browserlayer_removed(self):
        """Test that IPlonethemeFutureImperfectLayer is removed."""
        from plonetheme.future_imperfect.interfaces import IPlonethemeFutureImperfectLayer
        from plone.browserlayer import utils
        self.assertNotIn(IPlonethemeFutureImperfectLayer, utils.registered_layers())
