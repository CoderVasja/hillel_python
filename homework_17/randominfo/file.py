from __future__ import unicode_literals
import sys, glob, csv, pytz, shutil
from os import listdir, getcwd, access, W_OK
from os.path import abspath, join, dirname, split, exists, isfile, isdir
sys.path.append("/randominfo/")
from random import randint, choice, sample, randrange
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont
from math import ceil
full_path = lambda filename: abspath(join(dirname(__file__), filename))
with open(full_path('data.csv'), 'r') as f:
    print(f.read())