# -*- coding: utf-8 -*-
# Copyright (c) 2012-2014, Anima Istanbul
#
# This module is part of anima-tools and is released under the BSD 2
# License: http://www.opensource.org/licenses/BSD-2-Clause
from anima import ui
from anima.env import maya
from anima.ui import version_creator, models, version_updater
from anima.ui.scripts import do_db_setup


def version_creator():
    """Helper function for version_creator UI for Maya
    """
    # connect to db
    do_db_setup()

    # use PySide for Maya 2014
    import pymel
    try:
        if pymel.versions.current() >= pymel.versions.v2014:
            ui.SET_PYSIDE()
    except AttributeError:
        pass

    reload(version_creator)
    reload(models)
    m = maya.Maya()
    m.name = "Maya%s" % str(pymel.versions.current())[0:4]

    import logging
    logger = logging.getLogger('anima.ui.version_creator')
    logger.setLevel(logging.WARNING)
    logger = logging.getLogger('anima.ui.models')
    logger.setLevel(logging.WARNING)

    version_creator.UI(environment=m)


def version_updater():
    """helper function for version_updater UI for Maya
    """
    # connect to db
    do_db_setup()

    # use PySide for Maya 2014
    import pymel
    try:
        if pymel.versions.current() >= pymel.versions.v2014:
            from anima import ui
            ui.SET_PYSIDE()
    except AttributeError:
        pass

    from anima.ui import models
    from anima.env import maya
    reload(version_updater)
    reload(models)
    m = maya.Maya()
    m.name = "Maya" + str(pymel.versions.current())[0:4]

    import logging
    logger = logging.getLogger('anima.env.base')
    logger.setLevel(logging.WARNING)
    logger = logging.getLogger('anima.ui.version_updater')
    logger.setLevel(logging.WARNING)
    logger = logging.getLogger('anima.ui.models')
    logger.setLevel(logging.WARNING)

    # generate a reference_resolution
    version_updater.UI(environment=m)
