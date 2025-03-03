# RiveScript-Python
#
# This code is released under the MIT License.
# See the "LICENSE" file for more information.
#
# https://www.rivescript.com/

# Python 3 compat
from __future__ import print_function, unicode_literals

from .converscript import ConverScript
from .exceptions import (
    RiveScriptError, NoMatchError, NoReplyError, ObjectError,
    DeepRecursionError, NoDefaultRandomTopicError, RepliesNotSortedError
)

__author__ = 'Noah Petherbridge'
__copyright__ = 'Copyright 2015, Noah Petherbridge'
__credits__ = [
    'Noah Petherbridge',
    'dinever'
]
__license__ = 'MIT'
__maintainer__ = 'Noah Petherbridge'
__status__ = 'Production'
__docformat__ = 'plaintext'

__all__ = ['converscript.py']
__version__ = '1.14.9'
