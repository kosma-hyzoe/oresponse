from json_checker import Checker
import requests
from time import perf_counter, sleep


def __main__():
    x = 10
    y = 5

    # regex?
    json_schema = {
        "gS": str,
        "aS": str,
        "ahS": str,
        "iaS": str,
        "nS": str,
        "lS": "error"
    }

    with open("log.txt", 'w') as f:
        for i in range(0, x):
            start_time = perf_counter()
            raw_data = requests.get("https://tvgo.orange.pl/gpapi/status")

            response_time = perf_counter() - start_time
            http_response_code = raw_data.status_code

            try:
                data = raw_data.json()
            except (AttributeError, ValueError):
                is_json = False
            is_json = True

            checker = Checker(json_schema)
            if not checker.validate(data):
                is_valid_json = False
            is_valid_json = True

            output = f"data: {data}\nresponse_time: {response_time}\nhttp_response_code: {http_response_code}\n" \
                     f"is_json: {is_json}\nis_valid_json: {is_valid_json}\n"
            print(output)
            f.write(output + '\n')
            sleep(y -(perf_counter() - start_time))


if __name__ == '__main__':
    __main__()
