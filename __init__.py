import bpy
from .core import QtWindowEventLoop
from . import human
bl_info = {
    "name" : "PySide2_setup",
    "author" : "Harsh Jha",
    "description" : "First attempt to connect Qt-Python_blender",
    "blender" : (2, 80, 0),
    "version" : (0, 0, 1),
    "location" : "",
    "warning" : "",
    "category" : "Generic"
}

def register():
    bpy.utils.register_class(QtWindowEventLoop)
    bpy.utils.register_class(human.CustomWindowOperator)
    bpy.utils.register_class(human.CamControllerQtPanel)

def unregister():
    bpy.utils.unregister_class(QtWindowEventLoop)
    bpy.utils.unregister_class(human.CustomWindowOperator)
    bpy.utils.unregister_class(human.CamControllerQtPanel)