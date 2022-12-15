import time

from dcpd_aptitude import apti_main
from dcpd_verbal import verbal_main
from dcpd_logical import logical_main

username = ''
password = ''

apti_main(username, password)
time.sleep(1)

verbal_main(username, password)
time.sleep(1)

logical_main(username, password)
