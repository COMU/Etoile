#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Copyright 2009 TUBITAK/UEKAE
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/licenses/old-licenses/gpl-2.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir="gnustep-base-%s" % get.srcVERSION()
def setup():
    autotools.configure("--disable-importing-config-file")

def build():
    autotools.make()

def install():
    autotools.install()
    pisitools.dodoc("README","ChangeLog.*","COPYING")

