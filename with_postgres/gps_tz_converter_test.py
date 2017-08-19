import unittest

from with_postgres.gps_tz_converter import convert_gps_to_timezone


class TestTimeZoneCoordConverter(unittest.TestCase):
    def test_converter(self):
        self.assertEqual(convert_gps_to_timezone(latitude=37.776685, longitude=-122.420706, ), 'America/Los_Angeles')
        self.assertEqual(convert_gps_to_timezone(latitude=37.3880961, longitude=-5.9823299), 'Europe/Madrid')
        self.assertEqual(convert_gps_to_timezone(latitude=55.755826, longitude=37.6173), 'Europe/Moscow')
        self.assertNotEqual(convert_gps_to_timezone(longitude=55.755826, latitude=37.6173), 'Europe/Moscow')

if __name__ == "__main__":
    unittest.main()
