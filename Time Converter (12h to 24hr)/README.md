https://py.checkio.org/en/mission/time-converter-12h-to-24h/

Your task is to convert the time from the 12-h format into 24-h by following the next rules:
- the output format should be 'hh:mm'
- if the output hour is less than 10 - write '0' before it. For example: '09:05'

Input: Time in a 12-hour format (as a string).

Output: Time in a 24-hour format (as a string).

Example:

time_converter('12:30 p.m.') == '12:30'

time_converter('9:00 a.m.') == '09:00'

time_converter('11:15 p.m.') == '23:15'
