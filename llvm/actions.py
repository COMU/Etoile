#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
WorkDir="llvm-2.6"
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    autotools.configure("--enable-shared")

def build():
    autotools.make()

def install():
    pisitools.dodoc("README.txt","CREDITS.TXT","LICENSE.TXT")
    autotools.install()
