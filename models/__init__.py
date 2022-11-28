#!/bin/usr/python3
"""Init magic method overwriten"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
