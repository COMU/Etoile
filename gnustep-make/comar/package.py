#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

def postInstall():
    os.system('source /usr/System/Library/Makefiles/GNUstep.sh')

def preRemove():
    pass
