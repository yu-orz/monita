# -*- coding: utf-8 -*-
import urllib2
import sys
import smtplib
from datetime import datetime
from email.MIMEText import MIMEText
from email.Header import Header
from email.Utils import formatdate
from config import (TARGET_URLS,
                    DATETIME_FORMAT,
                    TIME_OUT_SECOND,
                    FROM_ADDRESS,
                    EMAILS,
                    MAIL_SUBJECT,
                    URL_OPEN_ERROR_MESSAGE,
                    STATUS_CODE_ERROR_MESSAGE,
                    MAIL_CHARSET,
                    SMTP_HOST,
                    SMTP_PORT)


def main():
    for url in TARGET_URLS:
        message = ''
        status_code = None
        try:
            response = urllib2.urlopen(url, timeout=TIME_OUT_SECOND)
            status_code = response.getcode()
        except:
            message = URL_OPEN_ERROR_MESSAGE.format(
                url=url,
                info=sys.exc_info(),
                datetime=datetime.now().strftime(DATETIME_FORMAT))
        else:
            if status_code == 200:
                print('{url:32s} - OK'.format(url=url))
            else:
                message += STATUS_CODE_ERROR_MESSAGE.format(
                    url=url,
                    datetime=datetime.now().strftime(DATETIME_FORMAT),
                    status_code=response.getcode(),
                    response_info=response.info()
                )

        if message:
            print(message)
            for email in EMAILS:
                subject = MAIL_SUBJECT.format(url=url)
                text = message
                msg = MIMEText(text.encode(MAIL_CHARSET),
                               "plain",
                               MAIL_CHARSET)
                msg["Subject"] = Header(subject, MAIL_CHARSET)
                msg["From"] = FROM_ADDRESS
                msg["To"] = email
                msg["Date"] = formatdate(localtime=True)
                smtp = smtplib.SMTP(SMTP_HOST, SMTP_PORT)
                smtp.sendmail(FROM_ADDRESS, email, msg.as_string())
                smtp.close()


if __name__ == '__main__':
    main()
