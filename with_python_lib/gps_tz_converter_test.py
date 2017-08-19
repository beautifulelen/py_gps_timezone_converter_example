import unittest
from with_python_lib.gps_tz_converter import GpsToTimezoneConverter


class TestTimeZoneCoordConverter2(unittest.TestCase):
    def setUp(self):
        self.converter = GpsToTimezoneConverter()

    def test_converter(self):
        self.assertEqual(self.converter.convert(latitude=37.776685, longitude=-122.420706, ), 'America/Los_Angeles')
        self.assertEqual(self.converter.convert(latitude=37.3880961, longitude=-5.9823299), 'Europe/Madrid')
        self.assertEqual(self.converter.convert(latitude=55.755826, longitude=37.6173), 'Europe/Moscow')
        self.assertNotEqual(self.converter.convert(longitude=55.755826, latitude=37.6173), 'Europe/Moscow')

if __name__ == "__main__":
    unittest.main()
