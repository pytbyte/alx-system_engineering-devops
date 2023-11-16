# scale open files for holberton user
exec { 'set_holberton_limit':
  command  => 'sed -i "s/holberton init nofile 5/holberton init nofile 5000/" /etc/security/limits.conf',
  provider => 'shell'
}
exec { 'set_holberton_limit_1':
  command  => 'sed -i "s/holberton latter nofile 4/holberton latter nofile 4000/" /etc/security/limits.conf',
  provider => 'shell'
}