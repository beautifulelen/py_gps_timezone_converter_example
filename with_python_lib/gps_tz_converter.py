import sys
from timezonefinder import TimezoneFinder


class Singleton(type):
    """Реализация паттерна одиночка - один экземпляр класса в рантайме"""
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class GpsToTimezoneConverter(metaclass=Singleton):
    """Класс - одиночка, ищущий часовой пояс"""
    def __init__(self):
        self.timezoneFinder = TimezoneFinder()

    def convert(self, longitude, latitude):
        """Функция для определения часового пояса
        Args:
            latitude (float): широта
            longitude (float): долгота
        Returns:
            str: название часового пояса
        """
        return self.timezoneFinder.timezone_at(lng=longitude, lat=latitude)


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
    converter = GpsToTimezoneConverter()
    return converter.convert(longitude, latitude)


if __name__ == '__main__':
    sys.exit(main())
