import datetime
import unittest
import unittest.mock as mock


class MockDatetimeTest(unittest.TestCase):

    def setUp(self):
        datetime_patcher = mock.patch.object(
            datetime, 'datetime',
            mock.Mock(wraps=datetime.datetime)
        )
        mocked_datetime = datetime_patcher.start()
        mocked_datetime.today.return_value = datetime.datetime(2012, 6, 16)
        self.addCleanup(datetime_patcher.stop)

    def test_datetime(self):
        self.assertEqual(
            datetime.datetime.today(),
            datetime.datetime(2012, 6, 16)
        )


class MockDatetimeDecoratorTest(unittest.TestCase):

    @mock.patch.object(datetime, 'datetime')
    def test_datetime(self, mocked_datetime):
        mocked_datetime.today.return_value = datetime.datetime(2012, 6, 16)
        self.assertEqual(
            datetime.datetime.today(),
            datetime.datetime(2012, 6, 16)
        )

if __name__ == '__main__':
    unittest.main()
