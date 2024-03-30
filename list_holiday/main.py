import requests
from models.holiday import Holiday


def get_holidays():
    try:
        headers = {"User-Agent": "ListHoliday/1.0"}
        response = requests.get("https://apis.digital.gob.cl/fl/feriados", headers=headers)
        response.raise_for_status()
        response_data = response.json()
        holidays = [Holiday(**holiday) for holiday in response_data]
        return holidays

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Network error when connecting to the holiday server: {e}")

    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error al decodificar la respuesta JSON: {e}")

    except Exception as e:
        # Catch any other unexpected errors
        print(f"Error inesperado: {e}")


def filter_holidays(holidays):
    filtered_holidays = []
    for holiday in holidays:
        if holiday.fecha.year > 2019:
            holiday.fecha = holiday.fecha.strftime("%Y-%m-%d")
            filtered_holidays.append(holiday)
    return filtered_holidays


def main():
    holidays = get_holidays()
    filtered_holidays = filter_holidays(holidays)
    print([data.fecha for data in filtered_holidays])


if __name__ == "__main__":
    main()
