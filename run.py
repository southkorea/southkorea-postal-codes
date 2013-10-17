# -*- coding: utf-8 -*-

from itertools import imap
import logging
import sys

import gevent
from gevent import monkey; monkey.patch_all()
from gevent.pool import Pool
import requests

from settings import *


## Constants ###
CODE_API_LIMIT_EXCEED = '41'


def read_postal_addresses(inpath):
    for line in open(inpath, 'r'):
        postal_code, address = line.decode(SOURCE_ENCODING).strip().split(',', 1)
        address = address.strip('"')
        postal_code = '%s-%s' % (postal_code[:3], postal_code[3:])
        yield (postal_code, address)


def addr2coord(address):
    url = API_URL + '&q=%s&output=json' % address
    r = requests.get(url, headers=HEADERS)
    response_data = r.json()

    try:
        items = response_data['channel']['item']
    except:
        if str(response_data['dcode']) == CODE_API_LIMIT_EXCEED:
            logging.exception('API limit exceeded')
            sys.exit(1)

        raise Exception(response_data['dmessage'])

    if not items:
        raise Exception('Address not found: %s' % encode(address))

    item = items[0]
    return (item['title'], item['lat'], item['lng'])


def get_latlng(postal_code, address, cache=None):
    if cache and postal_code in cache:
        return

    latlng = cache.get(address) if cache else None
    if not latlng:
        try:
            tup = addr2coord(address)
        except Exception as e:
            logging.exception(e.message)
            print '%s,,' % postal_code
            return

        if address != tup[0]:
            addr1, addr2 = map(encode, [address, tup[0]])
            logging.warning('Addresses do not match: %s | %s' % (addr1, addr2))

        latlng = (tup[1], tup[2])
        if cache:
            cache[address] = latlng

    if cache:
        cache[postal_code] = latlng

    logging.info('Processed %s' % postal_code)
    print '%s,%s,%s' % (postal_code, latlng[0], latlng[1])


def encode(s, encoding=OUTPUT_ENCODING):
    if isinstance(s, unicode):
        s = s.encode(encoding)
    elif not isinstance(s, str):
        s = str(s)
    return s


def main(inpath):
    cache = {}
    pool = Pool(POOL_SIZE)
    jobs = [pool.spawn(get_latlng, postal_code, address, cache)
            for postal_code, address in read_postal_addresses(inpath)]
    gevent.joinall(jobs)


def usage():
    print '''%s <sourcefile>

    sourcefile: csv file that contains (postal code, address) pairs.
''' % __file__


if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    main(*sys.argv[1:])

