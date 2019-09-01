# rivescript-python setup.py

import converscript
from setuptools import setup

setup(
    name             = 'converscript',
    version          = converscript.__version__,
    description      = 'A Chatterbot Scripting Language',
    long_description = 'A scripting language to make it easy to write responses for a chatterbot.',
    author           = 'Noah Petherbridge',
    author_email     = 'root@kirsle.net',
    url              = 'https://github.com/aichaos/converscript-python',
    license          = 'MIT',
    packages         = ['converscript'],
    keywords         = ['bot', 'chatbot', 'chatterbot', 'ai', 'aiml',
                        'chatscript', 'buddyscript'],
    classifiers      = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
    install_requires = [ 'setuptools', 'six' ],
)

# vim:expandtab
