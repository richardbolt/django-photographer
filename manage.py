#!/usr/bin/env python
import os
import sys

try:
    import mptt
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../django-mptt')))
try:
    import feincms
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../feincms')))
try:
    import form_designer
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../form_designer')))
try:
    import markupmirror
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../django-markupmirror')))
try:
    import elephantblog
except ImportError:
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../feincms-elephantblog')))


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "rboltphoto.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
