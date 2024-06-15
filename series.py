
import os

for dirpath, dirnames, filenames in os.walk('tests'):
    for filename in filenames:
        if filename.lower().endswith(('.pyc', '__init__.py')): continue

        module = ".".join([dirpath, filename.split('.')[0]])

        print (module)