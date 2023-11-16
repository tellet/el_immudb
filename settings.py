# -*- coding: utf-8 -*-
"""Describe project settings"""
import os

from dotenv import load_dotenv

load_dotenv()

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))
IMMUDB_BASE_URL = 'https://vault.immudb.io'
API_PATH = os.getenv('API_PATH')
X_API_KEY = os.getenv('X_API_KEY')
COLLECTION = os.getenv('COLLECTION', 'default')
LEDGER = os.getenv('LEDGER', 'default')
