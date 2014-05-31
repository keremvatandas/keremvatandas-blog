#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Kerem Vatandas'
SITENAME = u'\u03bb Kerem Vatandas \u2192 Personal Web Site'
SITEURL = 'http://www.keremvatandas.net'

SLOGAN = u'Open source software...'
ALT_SLOGAN = u'''
Malesef Turkiye'de yeteri kadar eleman yetistiren insan ve sirket yok...'''

THEME = 'responsive'

TIMEZONE = 'Europe/Istanbul'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (
    ('Pelican', 'http://getpelican.com/'),
    ('Python.org', 'http://python.org/'),
    ('Jinja2', 'http://jinja.pocoo.org/'),
)

# Social widget
SOCIAL = (
    ('Twitter', 'https://twitter.com/keremvatandas', '&#xe086;'),
    ('Github', 'https://github.com/keremvatandas', '&#xe037;'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = [
    'images',
    'theme/img/logo.jpg',
]

GOOGLE_ANALYTICS = 'UA-48632912-1'
DISQUS_SITENAME = 'keremvatandas'
