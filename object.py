# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 18:09:14 2021

@author: Ayaz
"""

import json

class Foo(object):
  def __init__(self, name, value):
    self.name = name
    self.value = value

myfoo = Foo('abc', 'xyz')
with open('foo.txt', 'w') as f:
  f.write(' '.join(["myfoo.%s = %s" % (k,v) for k,v in myfoo.__dict__.items()]))