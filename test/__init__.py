import unittest

modules = [
  'test.caesar',
]

suite = unittest.TestSuite()

for module_path in modules:
    try:
        module = __import__(module_path, globals(), locals(), ['suite'])
        test = getattr(module, 'suite')
        suite.addTest(test())
    except (ImportError, AttributeError):
        suite.addTest(unittest.defaultTestLoader.loadTestsFromName(module_path))

unittest.TextTestRunner().run(suite)