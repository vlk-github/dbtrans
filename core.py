# encoding=utf-8
import os
import warnings
import pymysql.cursors
from googletrans import Translator as BaseTranslator
from googletrans import urls, utils
from googletrans.constants import DEFAULT_USER_AGENT, LANGUAGES, SPECIAL_CASES