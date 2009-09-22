import logging

import sys
import pickle
import json
import glob
import codecs

from os import path
from pprint import pprint
from json import load
from sphinx.application import Sphinx
from datetime import datetime, tzinfo

log = logging.getLogger(__name__)

def dump():
    srcdir = path.abspath('.')
    confdir = path.abspath('_sphinx_config')
    outdir = path.abspath('_build')
    
    s = Sphinx(srcdir=srcdir,
               confdir=confdir,
               outdir=outdir,
               doctreedir=outdir + '/doctrees', #Never actually gonna use this
               buildername='json',
               confoverrides={},
               status=sys.stdout,
               )

    s.build(True, []) #TODO selectively choose files


    found_docs = [d for d in s.builder.env.found_docs if 'config/' not in d]

    for d in found_docs:
        data_path = '%s/%s.fjson' % (outdir, d)

        post = load(open(data_path))

        meta = post['meta']
    
        yaml = meta

        # this is a workaround because sphinx won't let us have a date
        # tag for some reason
        if 'post_date' in yaml:
            yaml['date'] = yaml['post_date']
            del(yaml['post_date'])

        yaml['format'] = 'html' # We are converting this to HTML

        if 'title' not in yaml:
            yaml['title'] = post['title']

        o = codecs.open('%s.html' % (d), 'w', encoding='ascii', errors='xmlcharrefreplace')
        with o:
            print >>o, u'---'.encode('UTF8')
            for k, v in yaml.iteritems():
                print >>o,  u'%s: %s' % (k, v)
            print >>o, u'---'
            print >>o, post['body']


