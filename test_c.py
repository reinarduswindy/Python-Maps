from ctypes import cdll
import ctypes
lib = cdll.LoadLibrary('./libtest.so')

class Foo(object):
    def __init__(self):
        self.obj = lib.test_new()

    def bar(self):
        st = lib.test_print(self.obj)
        return st

    def sayname(self, name):
    	name = name.encode('utf-8')
    	st = lib.test_hello(self.obj, name)
    	st = ctypes.c_char_p(st).value
    	return st.decode('utf-8')