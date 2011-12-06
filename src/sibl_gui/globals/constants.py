#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**constants.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines **Umbra** package default constants through the :class:`Constants` class.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import os
import platform

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["Constants"]

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class Constants():
	"""
	This class provides **Umbra** package default constants.
	"""

	applicationName = "sIBL_GUI"
	"""Package Application name: '**sIBL_GUI**' ( String )"""
	releaseVersion = "4.0.0"
	"""Package release version: '**4.0.0**' ( String )"""

	logger = "sIBL_GUI_Logger"
	"""Package logger name: '**sIBL_GUI_Logger**' ( String )"""

	applicationDirectory = "sIBL_GUI"
	"""Package Application directory: '**sIBL_GUI**' ( String )"""
	if platform.system() == "Windows" or platform.system() == "Microsoft" or platform.system() == "Darwin":
		providerDirectory = "HDRLabs"
		"""Package provider directory: '**HDRLabs** on Windows / Darwin, **.HDRLabs** on Linux' ( String )"""
	elif platform.system() == "Linux":
		providerDirectory = ".HDRLabs"
		"""Package provider directory: '**HDRLabs** on Windows / Darwin, **.HDRLabs** on Linux' ( String )"""

	databaseDirectory = "database"
	"""Application Database directory: '**database**' ( String )"""
	databaseMigrationsDirectory = "migrations"
	"""Application Database migrations directory: '**migrations**' ( String )"""
	databaseMigrationsFilesDirectory = "versions"
	"""Application Database migrations files versions directory: '**versions**' ( String )"""
	databaseMigrationsTemplatesDirectory = "templates"
	"""Application Database migrations templates files directory: '**templates**' ( String )"""
	patchesDirectory = "patches"
	"""Application patches directory: '**patches**' ( String )"""
	settingsDirectory = "settings"
	"""Application settings directory: '**settings**' ( String )"""
	userComponentsDirectory = "components"
	"""Application user components directory: '**components**' ( String )"""
	loggingDirectory = "logging"
	"""Application logging directory: '**logging**' ( String )"""
	templatesDirectory = "templates"
	"""Application templates directory: '**templates**' ( String )"""
	ioDirectory = "io"
	"""Application io directory: '**io**' ( String )"""


	preferencesDirectories = (databaseDirectory,
								patchesDirectory,
								settingsDirectory,
								userComponentsDirectory,
								loggingDirectory,
								templatesDirectory,
								ioDirectory)
	"""Application preferences directories ( Tuple )"""

	coreComponentsDirectory = "components/core"
	"""Application core components directory: '**components/core**' ( String )"""
	addonsComponentsDirectory = "components/addons"
	"""Application addons components directory: '**components/addons**' ( String )"""

	resourcesDirectory = "resources"
	"""Application resources directory: '**resources**' ( String )"""

	patchesFile = "sIBL_GUI_Patches.rc"
	"""Application settings file: '**sIBL_GUI_Patches.rc**' ( String )"""
	databaseFile = "sIBL_GUI_Database.sqlite"
	"""Application Database file: '**sIBL_GUI_Database.sqlite**' ( String )"""
	settingsFile = "sIBL_GUI_Settings.rc"
	"""Application settings file: '**sIBL_GUI_Settings.rc**' ( String )"""
	loggingFile = "sIBL_GUI_Logging.log"
	"""Application logging file: '**sIBL_GUI_Logging.log**' ( String )"""

	databaseMigrationsFilesExtension = "py"
	"""Application Database migrations files extension: '**py**' ( String )"""

	librariesDirectory = "libraries"
	"""Application libraries directory: '**libraries**' ( String )"""
	if platform.system() == "Windows" or platform.system() == "Microsoft":
		freeImageLibrary = os.path.join(librariesDirectory, "freeImage/resources/FreeImage.dll")
		"""FreeImage library path: '**freeImage/resources/FreeImage.dll** on Windows,
		**freeImage/resources/libfreeimage.dylib** on Darwin,
		**freeImage/resources/libfreeimage.so** on Linux' ( String )"""
	elif platform.system() == "Darwin":
		freeImageLibrary = os.path.join(librariesDirectory, "freeImage/resources/libfreeimage.dylib")
		"""FreeImage library path: '**freeImage/resources/FreeImage.dll** on Windows,
		**freeImage/resources/libfreeimage.dylib** on Darwin,
		**freeImage/resources/libfreeimage.so** on Linux' ( String )"""
	elif platform.system() == "Linux":
		freeImageLibrary = os.path.join(librariesDirectory, "freeImage/resources/libfreeimage.so")
		"""FreeImage library path: '**freeImage/resources/FreeImage.dll** on Windows,
		**freeImage/resources/libfreeimage.dylib** on Darwin,
		**freeImage/resources/libfreeimage.so** on Linux' ( String )"""
