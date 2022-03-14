# -*- coding: utf-8 -*-
"""
/***************************************************************************
 VectorTools
                                 A QGIS plugin
 Some QGIS vector processing algorithms.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                              -------------------
        begin                : 2022-02-28
        copyright            : (C) 2022 by szchixy
        email                : szchixy@outlook.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""

__author__ = 'szchixy'
__date__ = '2022-02-28'
__copyright__ = '(C) 2022 by szchixy'


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load VectorTools class from file VectorTools.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    from .vector_tools import VectorToolsPlugin
    return VectorToolsPlugin()
