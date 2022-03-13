# -*- coding: utf-8 -*-
"""
Created on 

@author: Manish Yadav
"""

import os

Dir = 'D:/Work/Programming/Projects/streamlit/PenguinsClassificationApp'

with open(os.path.join(Dir,'Procfile'), "w") as file1:
    toFile = 'web: sh setup.sh && streamlit run PenguinsApp.py'
    
file1.write(toFile)