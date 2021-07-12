#!/usr/bin/env python
#coding: utf8 

import os,random
setup = "/path_to_folder/" + random.choice(os.listdir("/path_to_folder/"))
os.system("DISPLAY=:0 GSETTINGS_BACKEND=dconf gsettings set org.gnome.desktop.background picture-uri  'file://%s'" %(setup))
