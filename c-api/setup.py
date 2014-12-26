from distutils.core import setup, Extension

spammodule = Extension('spam',
                       sources=['_spammodule.c'])

setup(
    name='Spam',
    version='1.0',
    description='This is a demo module.',
    ext_modules=[spammodule],
)
