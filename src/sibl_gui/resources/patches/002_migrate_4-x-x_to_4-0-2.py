#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**002_migrate_4-x-x_to_4-0-2.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module migrates sIBL_GUI from 4.x.x to 4.0.2.

**Others:**

"""
#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import logging
import os

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.common
import foundations.core as core
from umbra.globals.constants import Constants
from umbra.globals.runtimeGlobals import RuntimeGlobals

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2012 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["UID", "apply"]

LOGGER = logging.getLogger(Constants.logger)

UID = "00fd997f2a2c395b59aa31f1997f831b"

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
def apply():
	"""
	This definition is called by the Application and triggers the patch execution.

	:return: Definition success. ( Boolean )
	"""

	defaultScriptEditorDirectory = os.path.join(RuntimeGlobals.userApplicationDataDirectory,
														Constants.ioDirectory,
														"scriptEditor")
	defaultScriptEditorFile = os.path.join(defaultScriptEditorDirectory, "defaultScript.py")

	if foundations.common.pathExists(defaultScriptEditorFile):
		LOGGER.info("{0} | Removing deprecated '{1}' default script file!".format(
		core.getModule(apply).__name__, defaultScriptEditorFile))
		os.remove(defaultScriptEditorFile)
	return True
