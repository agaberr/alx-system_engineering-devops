# change config file for no errors
exec { '/usr/bin/env sed -i "s/holberton/foo/" /etc/security/limits.conf': }
