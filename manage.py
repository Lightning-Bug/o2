#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "o2.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)

   # Ek ladki baba ke paas gai .. Ladki : Baba ji mujhe bhavishay dekhna hai.. Baba : Thik hai , Kapde utaro aur ghodi ban jao.. Ladki : Baba Aap  mujhe chodna chate ho.. Baba : Dekha tum dekhne lagi na bhavishay….

#Source: http://funnyworldmarket.com/category/hindi-funny-jokes/dirty-jokes-hindi/
#© Funny World Market
