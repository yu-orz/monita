monita
======

simple http monitering python script

required python 2.6+ and a SMTP server

##how to use

1. rename config.sample.py to config.py

2. edit config.py. TARGET_URLS and EMAILS are required item.

3. set cronjob 

example:

    */5 * * * * python /path/to/monita/monita.py > /dev/null 2>&1
