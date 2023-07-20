import sys
from datetime import datetime
import requests
import xmltodict


def convert_date(date_str):
    try:
        # Convert the date string to a datetime object
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        # Format the datetime object as a string in the desired format
        formatted_date = date_obj.strftime("%d/%m/%Y")
    except  ValueError:
        return
    return formatted_date


def currency_rates(code, date):
    """ get currency value"""
    date = convert_date(date)
    params = {'date_req': date}
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
                      ' Chrome/112.0.0.0 YaBrowser/23.5.4.674 Yowser/2.5 Safari/537.36'
    }
    url = 'http://www.cbr.ru/scripts/XML_daily.asp'
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    text_response = response.text
    my_dict = xmltodict.parse(text_response)['ValCurs']['Valute']
    for dict_ in my_dict:
        if dict_.get('CharCode') == code:
            return f"{code} {dict_.get('Name')}: {dict_.get('Value')}"
    return my_dict[0]


if __name__ == "__main__":
    code = sys.argv[2].replace('--code=', '').strip()
    date = sys.argv[3].replace('--date=', '').strip()
    print(currency_rates(code, date))
