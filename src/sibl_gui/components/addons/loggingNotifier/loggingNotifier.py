#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**loggingNotifier.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines the :class:`LoggingNotifier` Component Interface class.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import logging
from PyQt4.QtCore import *
from PyQt4.QtGui import *

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.core as core
import foundations.exceptions
from manager.component import Component
from umbra.globals.constants import Constants

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2011 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "LoggingNotifier"]

LOGGER = logging.getLogger(Constants.logger)

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class LoggingNotifier(Component):
	"""
	| This class is the :mod:`umbra.components.addons.loggingNotifier.loggingNotifier` Component Interface class.
	| It displays Application logging messages in the Application status bar. The full Application logging history is available through the :mod:`umbra.components.addons.loggingWindow.loggingWindow` Component.
	"""

	@core.executionTrace
	def __init__(self, name=None):
		"""
		This method initializes the class.

		:param name: Component name. ( String )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		Component.__init__(self, name=name)

		# --- Setting class attributes. ---
		self.deactivatable = True

		self.__engine = None

		self.__memoryHandlerStackDepth = 0

	#******************************************************************************************************************
	#***	Attributes properties.
	#******************************************************************************************************************
	@property
	def engine(self):
		"""
		This method is the property for **self.__engine** attribute.

		:return: self.__engine. ( QObject )
		"""

		return self.__engine

	@engine.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def engine(self, value):
		"""
		This method is the setter method for **self.__engine** attribute.

		:param value: Attribute value. ( QObject )
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "engine"))

	@engine.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def engine(self):
		"""
		This method is the deleter method for **self.__engine** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "engine"))

	@property
	def memoryHandlerStackDepth(self):
		"""
		This method is the property for **self.__memoryHandlerStackDepth** attribute.

		:return: self.__memoryHandlerStackDepth. ( Integer )
		"""

		return self.__memoryHandlerStackDepth

	@memoryHandlerStackDepth.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def memoryHandlerStackDepth(self, value):
		"""
		This method is the setter method for **self.__memoryHandlerStackDepth** attribute.

		:param value: Attribute value. ( Integer )
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "memoryHandlerStackDepth"))

	@memoryHandlerStackDepth.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def memoryHandlerStackDepth(self):
		"""
		This method is the deleter method for **self.__memoryHandlerStackDepth** attribute.
		"""

		raise foundations.exceptions.ProgrammingError("{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "memoryHandlerStackDepth"))

	#******************************************************************************************************************
	#***	Class methods.
	#******************************************************************************************************************
	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def activate(self, engine):
		"""
		This method activates the Component.

		:param engine: Engine to attach the Component to. ( QObject )
		:return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Activating '{0}' Component.".format(self.__class__.__name__))

		self.__engine = engine

		self.activated = True
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def deactivate(self):
		"""
		This method deactivates the Component.

		:return: Method success. ( Boolean )
		"""

		LOGGER.debug("> Deactivating '{0}' Component.".format(self.__class__.__name__))

		self.__engine = None

		self.activated = False
		return True

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def initialize(self):
		"""
		This method initializes the Component.
		"""

		LOGGER.debug("> Initializing '{0}' Component.".format(self.__class__.__name__))

		# Signals / Slots.
		self.__engine.timer.timeout.connect(self.__statusBar_showLoggingMessages)

	@core.executionTrace
	@foundations.exceptions.exceptionsHandler(None, False, Exception)
	def uninitialize(self):
		"""
		This method uninitializes the Component.
		"""

		LOGGER.debug("> Uninitializing '{0}' Component.".format(self.__class__.__name__))

		# Signals / Slots.
		self.__engine.timer.timeout.disconnect(self.__statusBar_showLoggingMessages)

	# @core.executionTrace
	def __statusBar_showLoggingMessages(self):
		"""
		This method updates the engine status bar with logging messages.
		"""

		memoryHandlerStackDepth = len(self.__engine.loggingSessionHandlerStream.stream)

		if memoryHandlerStackDepth != self.__memoryHandlerStackDepth:
			for index in range(self.__memoryHandlerStackDepth, memoryHandlerStackDepth):
				self.__engine.statusBar.showMessage(self.__engine.loggingSessionHandlerStream.stream[index])
			self.__memoryHandlerStackDepth = memoryHandlerStackDepth
