#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**testsUiConstants.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines units tests for :mod:`sibl_gui.globals.uiConstants` module.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import re
import unittest

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
from sibl_gui.globals.uiConstants import UiConstants

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["UiConstantsTestCase"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class UiConstantsTestCase(unittest.TestCase):
	"""
	This class defines :class:`sibl_gui.globals.uiConstants.UiConstants` class units tests methods.
	"""

	def testRequiredAttributes(self):
		"""
		This method tests presence of required attributes.
		"""

		requiredAttributes = ("uiFile",
								"windowsStylesheetFile",
								"darwinStylesheetFile",
								"linuxStylesheetFile",
								"windowsStyle",
								"darwinStyle",
								"settingsFile",
								"linuxStyle",
								"layoutsFile",
								"applicationWindowsIcon",
								"applicationDarwinIcon",
								"splashScreenImage",
								"logoImage",
								"defaultToolbarIconSize",
								"centralWidgetIcon",
								"centralWidgetHoverIcon",
								"centralWidgetActiveIcon",
								"layoutIcon",
								"layoutHoverIcon",
								"layoutActiveIcon",
								"miscellaneousIcon",
								"miscellaneousHoverIcon",
								"miscellaneousActiveIcon",
								"libraryIcon",
								"libraryHoverIcon",
								"libraryActiveIcon",
								"inspectIcon",
								"inspectHoverIcon",
								"inspectActiveIcon",
								"exportIcon",
								"exportHoverIcon",
								"exportActiveIcon",
								"editIcon",
								"editHoverIcon",
								"editActiveIcon",
								"preferencesIcon",
								"preferencesHoverIcon",
								"preferencesActiveIcon",
								"formatErrorImage",
								"missingImage",
								"loadingImage",
								"startupLayout",
								"helpFile",
								"apiFile",
								"nativeImageFormats",
								"thirdPartyImageFormats")

		for attribute in requiredAttributes:
			self.assertIn(attribute, UiConstants.__dict__)

	def testUiFileAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.uiFile` attribute.
		"""

		self.assertRegexpMatches(UiConstants.uiFile, "\w+")

	def testWindowsStylesheetFileAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.windowsStylesheetFile` attribute.
		"""

		self.assertRegexpMatches(UiConstants.windowsStylesheetFile, "\w+")

	def testDarwinStylesheetFileAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.darwinStylesheetFile` attribute.
		"""

		self.assertRegexpMatches(UiConstants.darwinStylesheetFile, "\w+")

	def testLinuxStylesheetFileAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.linuxStylesheetFile` attribute.
		"""

		self.assertRegexpMatches(UiConstants.linuxStylesheetFile, "\w+")

	def testWindowsStyleAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.windowsStyle` attribute.
		"""

		self.assertRegexpMatches(UiConstants.windowsStyle, "\w+")

	def testDarwinStyleAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.darwinStyle` attribute.
		"""

		self.assertRegexpMatches(UiConstants.darwinStyle, "\w+")

	def testSettingsFileAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.settingsFile` attribute.
		"""

		self.assertRegexpMatches(UiConstants.settingsFile, "\w+")

	def testLinuxStyleAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.linuxStyle` attribute.
		"""

		self.assertRegexpMatches(UiConstants.linuxStyle, "\w+")

	def testLayoutsFileAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.layoutsFile` attribute.
		"""

		self.assertRegexpMatches(UiConstants.layoutsFile, "\w+")

	def testApplicationWindowsIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.applicationWindowsIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.applicationWindowsIcon, "\w+")
		self.assertRegexpMatches(UiConstants.applicationWindowsIcon, "\.[pP][nN][gG]$")

	def testApplicationDarwinIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.applicationDarwinIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.applicationDarwinIcon, "\w+")
		self.assertRegexpMatches(UiConstants.applicationDarwinIcon, "\.[pP][nN][gG]$")

	def testSplashscreemImageAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.splashScreenImage` attribute.
		"""

		self.assertRegexpMatches(UiConstants.splashScreenImage, "\w+")
		self.assertRegexpMatches(UiConstants.splashScreenImage,
								"\.[bB][mM][pP]$|\.[jJ][pP][eE][gG]$|\.[jJ][pP][gG]|\.[pP][nN][gG]$")

	def testLogoImageAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.logoImage` attribute.
		"""

		self.assertRegexpMatches(UiConstants.logoImage, "\w+")
		self.assertRegexpMatches(UiConstants.logoImage,
								"\.[bB][mM][pP]$|\.[jJ][pP][eE][gG]$|\.[jJ][pP][gG]|\.[pP][nN][gG]$")

	def testDefaultToolbarIconSizeAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.defaultToolbarIconSize` attribute.
		"""

		self.assertIsInstance(UiConstants.defaultToolbarIconSize, int)
		self.assertGreaterEqual(UiConstants.defaultToolbarIconSize, 8)
		self.assertLessEqual(UiConstants.defaultToolbarIconSize, 128)

	def testCentralWidgetIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.centralWidgetIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.centralWidgetIcon, "\w+")

	def testCentralWidgetHoverIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.centralWidgetHoverIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.centralWidgetHoverIcon, "\w+")

	def testCentralWidgetActiveIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.centralWidgetActiveIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.centralWidgetActiveIcon, "\w+")

	def testLayoutIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.layoutIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.layoutIcon, "\w+")

	def testLayoutHoverIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.layoutHoverIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.layoutHoverIcon, "\w+")

	def testLayoutActiveIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.layoutActiveIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.layoutActiveIcon, "\w+")

	def testMiscellaneousIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.miscellaneousIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.miscellaneousIcon, "\w+")

	def testMiscellaneousHoverIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.miscellaneousHoverIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.miscellaneousHoverIcon, "\w+")

	def testMiscellaneousActiveIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.miscellaneousActiveIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.miscellaneousActiveIcon, "\w+")

	def testLibraryIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.libraryIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.libraryIcon, "\w+")

	def testLibraryHoverIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.libraryHoverIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.libraryHoverIcon, "\w+")

	def testLibraryActiveIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.libraryActiveIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.libraryActiveIcon, "\w+")

	def testInspectIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.inspectIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.inspectIcon, "\w+")

	def testInspectHoverIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.inspectHoverIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.inspectHoverIcon, "\w+")

	def testInspectActiveIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.inspectActiveIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.inspectActiveIcon, "\w+")

	def testExportIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.exportIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.exportIcon, "\w+")

	def testExportHoverIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.exportHoverIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.exportHoverIcon, "\w+")

	def testExportActiveIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.exportActiveIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.exportActiveIcon, "\w+")

	def testEditIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.editIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.editIcon, "\w+")

	def testEditHoverIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.editHoverIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.editHoverIcon, "\w+")

	def testEditActiveIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.editActiveIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.editActiveIcon, "\w+")

	def testPreferencesIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.preferencesIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.preferencesIcon, "\w+")

	def testPreferencesHoverIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.preferencesHoverIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.preferencesHoverIcon, "\w+")

	def testPreferencesActiveIconAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.preferencesActiveIcon` attribute.
		"""

		self.assertRegexpMatches(UiConstants.preferencesActiveIcon, "\w+")

	def testFormatErrorImageAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.formatErrorImage` attribute.
		"""

		self.assertRegexpMatches(UiConstants.formatErrorImage, "\w+")
		self.assertRegexpMatches(UiConstants.formatErrorImage,
								"\.[bB][mM][pP]$|\.[jJ][pP][eE][gG]$|\.[jJ][pP][gG]|\.[pP][nN][gG]$")

	def testMissingImageAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.missingImage` attribute.
		"""

		self.assertRegexpMatches(UiConstants.missingImage, "\w+")
		self.assertRegexpMatches(UiConstants.missingImage,
								"\.[bB][mM][pP]$|\.[jJ][pP][eE][gG]$|\.[jJ][pP][gG]|\.[pP][nN][gG]$")

	def testLoadingImageAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.loadingImage` attribute.
		"""

		self.assertRegexpMatches(UiConstants.loadingImage, "\w+")
		self.assertRegexpMatches(UiConstants.loadingImage,
								"\.[bB][mM][pP]$|\.[jJ][pP][eE][gG]$|\.[jJ][pP][gG]|\.[pP][nN][gG]$")

	def testStartupLayoutAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.startupLayout` attribute.
		"""

		self.assertRegexpMatches(UiConstants.startupLayout, "\w+")

	def testHelpFileAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.helpFile` attribute.
		"""

		self.assertRegexpMatches(UiConstants.helpFile, "(http|ftp|https)://([a-zA-Z0-9\-\.]+)/?")

	def testApiFileAttribute(self):
		"""
		This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.apiFile` attribute.
		"""

		self.assertRegexpMatches(UiConstants.apiFile, "(http|ftp|https)://([a-zA-Z0-9\-\.]+)/?")

	def testNativeImageFormatsAttribute(self):
			"""
			This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.nativeImageFormats` attribute.
			"""

			self.assertIsInstance(UiConstants.nativeImageFormats, dict)
			for key, value in UiConstants.nativeImageFormats.iteritems():
				self.assertIsInstance(key, str)
				self.assertIsInstance(value, str)
				self.assertTrue(re.compile(value))

	def testThirdPartyImageFormatsAttribute(self):
			"""
			This method tests :attr:`sibl_gui.globals.uiConstants.UiConstants.thirdPartyImageFormats` attribute.
			"""

			self.assertIsInstance(UiConstants.thirdPartyImageFormats, dict)
			for key, value in UiConstants.thirdPartyImageFormats.iteritems():
				self.assertIsInstance(key, str)
				self.assertIsInstance(value, str)
				self.assertTrue(re.compile(value))

if __name__ == "__main__":
	unittest.main()
