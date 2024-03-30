import requests
import unittest
from datetime import datetime
from unittest.mock import patch, MagicMock
from list_holiday.main import get_holidays
from models.holiday import Holiday, Laws


class TestGetHolidays(unittest.TestCase):

    # Mocking a successful response from the API
    @patch("list_holiday.main.requests.get")
    def test_get_holidays_success(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = [
            {
                "nombre": "Año Nuevo",
                "comentarios": "",
                "fecha": "2018-01-01",
                "irrenunciable": "1",
                "tipo": "Civil",
                "leyes": [
                    {
                        "nombre": "Ley 2.977",
                        "url": "http://www.leychile.cl/Navegar?idNorma=23639",
                    },
                    {
                        "nombre": "Ley 19.973",
                        "url": "http://www.leychile.cl/Navegar?idNorma=230132",
                    },
                ],
            },
            {
                "nombre": "Inmaculada Concepción",
                "comentarios": " ",
                "fecha": "2018-12-08",
                "irrenunciable": "0",
                "tipo": "Religioso",
                "leyes": [
                    {
                        "nombre": "Ley 2.977",
                        "url": "http://www.leychile.cl/Navegar?idNorma=23639",
                    }
                ],
            },
            {
                "nombre": "Día Nacional del Trabajo",
                "comentarios": " ",
                "fecha": "2024-05-01",
                "irrenunciable": "1",
                "tipo": "Civil",
            },
        ]
        mock_get.return_value = mock_response
        holidays = get_holidays()
        self.assertEqual(len(holidays), 3)


    # Mocking a network error when making the API request
    @patch("list_holiday.main.requests.get")
    def test_get_holidays_network_error(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException("Connection error")
        holidays = get_holidays()
        self.assertIsNone(holidays)


    # Mocking a successful response from the API but with JSON decoding error
    @patch("list_holiday.main.requests.get")
    def test_get_holidays_json_error(self, mock_get):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError("JSON decoding error")
        mock_get.return_value = mock_response
        holidays = get_holidays()
        self.assertIsNone(holidays)


    # Create a valid instance of the Holiday model
    def test_holiday_model(self):
        holiday_data = {
            "nombre": "Christmas",
            "comentarios": "Festive season",
            "fecha": "2024-12-25",
            "irrenunciable": True,
            "tipo": "Public",
            "leyes": [{"nombre": "Holiday Act", "url": "https://example.com/holiday"}],
        }
        holiday = Holiday(**holiday_data)

        self.assertIsInstance(holiday, Holiday)
        self.assertEqual(holiday.nombre, "Christmas")
        self.assertEqual(holiday.comentarios, "Festive season")
        self.assertEqual(holiday.fecha, datetime(2024, 12, 25))
        self.assertTrue(holiday.irrenunciable)
        self.assertEqual(holiday.tipo, "Public")
        self.assertIsInstance(holiday.leyes[0], Laws)


    # Test the comments validator with valid and invalid input
    def test_validate_comments(self):
        valid_comment = "This is a valid comment"
        invalid_comment = ""

        # Validate valid comment
        validated_comment = Holiday.validate_comments(valid_comment)
        self.assertEqual(validated_comment, valid_comment)

        # Validate invalid comment
        validated_comment = Holiday.validate_comments(invalid_comment)
        self.assertIsNone(validated_comment)


    # Test the date validator with a valid date string
    def test_validate_date(self):
        valid_date_str = "2024-12-25"
        validated_date = Holiday.validate_date(valid_date_str)
        expected_date = datetime(2024, 12, 25)
        self.assertEqual(validated_date, expected_date)

        # Test the date validator with an invalid date string
        invalid_date_str = "2024-02-30"
        with self.assertRaises(ValueError):
            Holiday.validate_date(invalid_date_str)


if __name__ == "__main__":
    unittest.main()
