#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
**models.py**

**Platform:**
	Windows, Linux, Mac Os X.

**Description:**
	This module defines the :class:`sibl_gui.components.core.databaseBrowser.databaseBrowser.DatabaseBrowser`
	Component Interface class Workers.

**Others:**

"""

#**********************************************************************************************************************
#***	External imports.
#**********************************************************************************************************************
import logging
import os
from PyQt4.QtCore import QThread
from PyQt4.QtCore import QTimer
from PyQt4.QtCore import Qt
from PyQt4.QtCore import pyqtSignal

#**********************************************************************************************************************
#***	Internal imports.
#**********************************************************************************************************************
import foundations.common
import foundations.core as core
import foundations.exceptions
import sibl_gui.components.core.db.utilities.common as dbCommon
from umbra.globals.constants import Constants

#**********************************************************************************************************************
#***	Module attributes.
#**********************************************************************************************************************
__author__ = "Thomas Mansencal"
__copyright__ = "Copyright (C) 2008 - 2012 - Thomas Mansencal"
__license__ = "GPL V3.0 - http://www.gnu.org/licenses/"
__maintainer__ = "Thomas Mansencal"
__email__ = "thomas.mansencal@gmail.com"
__status__ = "Production"

__all__ = ["LOGGER", "DatabaseBrowser_worker"]

LOGGER = logging.getLogger(Constants.logger)

#**********************************************************************************************************************
#***	Module classes and definitions.
#**********************************************************************************************************************
class DatabaseBrowser_worker(QThread):
	"""
	This class is a `QThread <http://doc.qt.nokia.com/qthread.html>`_ subclass used
	to track modified Ibl Sets and update the Database accordingly.
	"""

	# Custom signals definitions.
	databaseChanged = pyqtSignal(list)
	"""
	This signal is emited by the :class:`DatabaseBrowser_worker` class
	when database Ibl Sets have been updated. ( pyqtSignal )
	
	:return: Updated Ibl Sets. ( List )		
	"""

	@core.executionTrace
	def __init__(self, parent):
		"""
		This method initializes the class.

		:param parent: Object parent. ( QObject )
		"""

		LOGGER.debug("> Initializing '{0}()' class.".format(self.__class__.__name__))

		QThread.__init__(self, parent)

		# --- Setting class attributes. ---
		self.__container = parent

		self.__dbSession = self.__container.coreDb.dbSessionMaker()

		self.__timer = None
		self.__timerCycleMultiplier = 5

	#******************************************************************************************************************
	#***	Attributes properties.
	#******************************************************************************************************************
	@property
	def container(self):
		"""
		This method is the property for **self.__container** attribute.

		:return: self.__container. ( QObject )
		"""

		return self.__container

	@container.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def container(self, value):
		"""
		This method is the setter method for **self.__container** attribute.

		:param value: Attribute value. ( QObject )
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "container"))

	@container.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def container(self):
		"""
		This method is the deleter method for **self.__container** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "container"))

	@property
	def dbSession(self):
		"""
		This method is the property for **self.__dbSession** attribute.

		:return: self.__dbSession. ( Object )
		"""

		return self.__dbSession

	@dbSession.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def dbSession(self, value):
		"""
		This method is the setter method for **self.__dbSession** attribute.

		:param value: Attribute value. ( Object )
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "dbSession"))

	@dbSession.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def dbSession(self):
		"""
		This method is the deleter method for **self.__dbSession** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "dbSession"))

	@property
	def timer(self):
		"""
		This method is the property for **self.__timer** attribute.

		:return: self.__timer. ( QTimer )
		"""

		return self.__timer

	@timer.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def timer(self, value):
		"""
		This method is the setter method for **self.__timer** attribute.

		:param value: Attribute value. ( QTimer )
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "timer"))

	@timer.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def timer(self):
		"""
		This method is the deleter method for **self.__timer** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "timer"))

	@property
	def timerCycleMultiplier(self):
		"""
		This method is the property for **self.__timerCycleMultiplier** attribute.

		:return: self.__timerCycleMultiplier. ( Float )
		"""

		return self.__timerCycleMultiplier

	@timerCycleMultiplier.setter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def timerCycleMultiplier(self, value):
		"""
		This method is the setter method for **self.__timerCycleMultiplier** attribute.

		:param value: Attribute value. ( Float )
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is read only!".format(self.__class__.__name__, "timerCycleMultiplier"))

	@timerCycleMultiplier.deleter
	@foundations.exceptions.exceptionsHandler(None, False, foundations.exceptions.ProgrammingError)
	def timerCycleMultiplier(self):
		"""
		This method is the deleter method for **self.__timerCycleMultiplier** attribute.
		"""

		raise foundations.exceptions.ProgrammingError(
		"{0} | '{1}' attribute is not deletable!".format(self.__class__.__name__, "timerCycleMultiplier"))

	#******************************************************************************************************************
	#***	Class methods.
	#******************************************************************************************************************
	@core.executionTrace
	def run(self):
		"""
		This method reimplements the :meth:`QThread.run` method.
		"""

		self.__timer = QTimer()
		self.__timer.moveToThread(self)
		self.__timer.start(Constants.defaultTimerCycle * self.__timerCycleMultiplier)

		self.__timer.timeout.connect(self.__updateIblSets, Qt.DirectConnection)

		self.exec_()

	@core.executionTrace
	def __updateIblSets(self):
		"""
		This method updates Database Ibl Sets if they have been modified on disk.
		"""

		modifiedIblSets = []
		for iblSet in dbCommon.getIblSets(self.__dbSession):
			if not foundations.common.pathExists(iblSet.path):
				continue

			storedStats = iblSet.osStats.split(",")
			osStats = os.stat(iblSet.path)
			if str(osStats[8]) == str(storedStats[8]):
				continue

			LOGGER.debug("> '{0}' Ibl Set file has been modified and will be updated!".format(iblSet.title))
			if dbCommon.updateIblSetContent(self.__dbSession, iblSet):
				LOGGER.debug("> '{0}' Ibl Set has been updated!".format(iblSet.title))
				modifiedIblSets.append(iblSet)

		modifiedIblSets and self.databaseChanged.emit(modifiedIblSets)
