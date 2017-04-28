#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json	# .loads
import requests	# .get

__author__ = "Adam Domagalski"
__email__ = "adadom@st.amu.edu.pl"
__date__ = "2017-04-28"


url = 'https://api.github.com/users/allegro/repos?sort=pushed&direction=desc'
req = requests.get(url)

data = json.loads(req.content)

print ('Last modified repository' +
	'\n\tRepo name: ' + data[0]['name'] +
	'\n\tLast modified: ' + 
	data[0]['pushed_at'].replace("T"," at ").replace("Z",""))

