from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reset the sequence of bibliotecaAPP_loan table'

    def handle(self, *args, **options):
        # Cierra cualquier conexión abierta a la base de datos
        connection.close()

        # Crea una nueva tabla "bibliotecaAPP_loan_new" con la misma estructura
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE bibliotecaAPP_loan_new AS SELECT * FROM bibliotecaAPP_loan WHERE 1=0;")

        # Elimina la tabla original "bibliotecaAPP_loan"
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE bibliotecaAPP_loan;")

        # Renombra la nueva tabla a "bibliotecaAPP_loan"
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE bibliotecaAPP_loan_new RENAME TO bibliotecaAPP_loan;")

        self.stdout.write(self.style.SUCCESS('Successfully reset the sequence of bibliotecaAPP_loan table.'))

from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Reset the sequence of bibliotecaAPP_loan table'

    def handle(self, *args, **options):
        # Cierra cualquier conexión abierta a la base de datos
        connection.close()

        # Crea una nueva tabla "bibliotecaAPP_loan_new" con la misma estructura, incluyendo la columna "id"
        with connection.cursor() as cursor:
            cursor.execute("CREATE TABLE bibliotecaAPP_loan_new AS SELECT * FROM bibliotecaAPP_loan WHERE 1=0;")

        # Elimina la tabla original "bibliotecaAPP_loan"
        with connection.cursor() as cursor:
            cursor.execute("DROP TABLE bibliotecaAPP_loan;")

        # Renombra la nueva tabla a "bibliotecaAPP_loan"
        with connection.cursor() as cursor:
            cursor.execute("ALTER TABLE bibliotecaAPP_loan_new RENAME TO bibliotecaAPP_loan;")

        self.stdout.write(self.style.SUCCESS('Successfully reset the sequence of bibliotecaAPP_loan table.'))
