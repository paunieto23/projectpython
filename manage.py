"""
manage.py

Eina principal per executar comandes de gestió de Django des de la línia de comandes.

Permet accedir a ordres com:
- runserver
- migrate
- createsuperuser
- test
i moltes més.
"""

#!/usr/bin/env python
import os
import sys

if __name__ == '__main__':
    # Defineix el mòdul de configuració per defecte del projecte
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'my_site.settings')
    try:
        # Importa i executa el sistema de comandes de Django
        from django.core.management import execute_from_command_line
    except ImportError:
        raise
    execute_from_command_line(sys.argv)
