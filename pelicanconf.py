#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Simone'
SITENAME = u"SiSo's Blog"
SITEURL = 'http://blog.idsiso.com'

PATH = 'content'

TIMEZONE = 'Australia/Sydney'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/soldasimo'),
          ('github', 'https://github.com/siso'),
          ('linkedin', 'http://au.linkedin.com/in/simonesoldateschi'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

import os.path
THEME = os.path.expanduser('~/workspace/pelican-themes/bootstrap2')

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
