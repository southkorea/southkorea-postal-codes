# -*- coding: utf-8 -*-

__all__ = ['API_KEY', 'API_URL', 'HEADERS', 'POOL_SIZE',
           'SOURCE_ENCODING', 'OUTPUT_ENCODING']

API_KEY = ''                 # Fill this
HEADERS = { 'referer': '' }  # Fill this
POOL_SIZE = 20
SOURCE_ENCODING = 'cp949'
OUTPUT_ENCODING = 'utf-8'

if not API_KEY:
    raise Exception('API key is mandatory.')
API_URL = 'http://apis.daum.net/local/geo/addr2coord?apikey=%s' % API_KEY

