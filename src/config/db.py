import mariadb
config = {
    'host': 'localhost',
    'port': 3308,
    'user': 'root',
    'password': '',
    'database': 'p2_asistencia_actividades'
}

DB = mariadb.connect(**config)
DB.autocommit = True