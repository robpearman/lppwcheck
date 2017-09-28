#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  lppwcheck.py
#  
#  Copyright 2017 Rob Pearman <rob.pearman@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import csv
import hashlib
import httplib
import time

def main(args):

    with open('lpdl/export.csv') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:

            name = row['name']
            pwd = row['password']

            # Ignore blank passwords (this includes secure notes)
            if pwd <> '':
                print 'Checking ' + name
                sha1 = hashlib.sha1(pwd).hexdigest()
                hibp = httplib.HTTPSConnection('haveibeenpwned.com')
                header = {'User-Agent': 'Pwnage-Checker-For-LastPass'}
                requrl = 'https://haveibeenpwned.com/api/v2/pwnedpassword/' + sha1
                hibp.request('GET', requrl, '', header)
                resp = hibp.getresponse()

                if resp.status == 200:
                    print 'Pwned password found for ' + name
                else:
                    if resp.status <> 404:
                        print 'Unknown status: ', resp.status, resp.reason

                time.sleep(1.6)

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
