import requests

def get_holidays():
    try:
        headers = {"User-Agent": "ListHoliday/1.0"}
        response = requests.get("https://apis.digital.gob.cl/fl/feriados", headers=headers)
        print(response)

    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Network error when connecting to the holiday server: {e}")
    
    except ValueError as e:
        # Handle JSON decoding errors
        print(f"Error al decodificar la respuesta JSON: {e}")
    
    except Exception as e:
        # Catch any other unexpected errors
        print(f"Error inesperado: {e}")
    
get_holidays()