# -*- coding: utf-8 -*-

TARGET_URLS = (
    'http://www.google.com/',
    'http://www.yahoo.com/',
)

DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'

TIME_OUT_SECOND = 3

FROM_ADDRESS = 'info@example.com'

EMAILS = (
    'member1@example.com',
    'member2@example.com',
)

MAIL_SUBJECT = 'Access Error {url}'

STATUS_CODE_ERROR_MESSAGE = """{url:32s} - Error

Url :        {url}
Datetime   : {datetime}
Status Code: {status_code}
Info:        {response_info}
"""

URL_OPEN_ERROR_MESSAGE = """{url:32s} - Error

Datetime   : {datetime}
{info[0]}
{info[1]}
"""

MAIL_CHARSET = 'utf-8'

SMTP_HOST = 'localhost'

SMTP_PORT = '25'
