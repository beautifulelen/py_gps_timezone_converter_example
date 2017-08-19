import configparser
import sys
import psycopg2


CONFIG_FILENAME = 'with_postgres\config.ini'


def get_database_configuration():
    """
    Функция возвращает настройки базы данных из файла конфигураций
    Returns:
        dict
    """
    try:
        with open(CONFIG_FILENAME) as fp:
            config = configparser.ConfigParser()
            config.read_file(fp)
            main_section = 'db_settings'
            return {
                'host': config.get(main_section, 'host'),
                'user': config.get(main_section, 'user'),
                'password': config.get(main_section, 'password'),
                'dbname': config.get(main_section, 'dbname')
            }
    except FileNotFoundError as err:
        print('File {0} not found: {1}'.format(CONFIG_FILENAME, err.strerror))
        sys.exit(1)
    except IOError:
        sys.exit(sys.exc_info()[0])


def get_database_connection():
    """
    Функция создающая соединение с базой данных
    Returns:
        psycopg2.connection
    """
    db_config = get_database_configuration()
    try:
        connection = psycopg2.connect(
                                host=db_config['host'],
                                dbname=db_config['dbname'],
                                user=db_config['user'],
                                password=db_config['password'])
    except psycopg2.DatabaseError as err:
        print('Database connection error: ', err)
        sys.exit(1)
    return connection


def convert_gps_to_timezone(latitude, longitude):
    """
    Функция определяющая часовой пояс
    Args:
        latitude (float): широта
        longitude (float): долгота
    Returns:
        str: название часового пояса
    """
    if latitude is None:
        raise TypeError('missing latitude param')
    if longitude is None:
        raise TypeError('missing longitude param')
    with get_database_connection() as connection:
        cursor = connection.cursor()
        query = '''
                SELECT * FROM get_tzname_by_gps({longitude}, {latitude})
                '''.format(longitude=longitude, latitude=latitude)
        cursor.execute(query)
        results = cursor.fetchone()
        if results and len(results) == 1:
            return results[0]


def main(argv=None):
    """
    Функция для вызова программы из консоли
    Args:
        *argv: Список аргументов переменной длины.
    Returns:
        str: название часового пояса
    """
    if argv is None:
            argv = sys.argv
    latitude = argv[1]
    longitude = argv[2]
    return convert_gps_to_timezone(latitude, longitude)


if __name__ == '__main__':
    sys.exit(main())
