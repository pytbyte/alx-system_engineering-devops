# scale open files for holberton user
exec { 'hard_limit':
  command  => 'sed -i "s/holberton hard nofile 5/holberton hard nofile 5000/" /etc/security/limits.conf',
  provider => 'shell'
}
exec { 'soft_limit':
  command  => 'sed -i "s/holberton soft nofile 4/holberton soft nofile 4000/" /etc/security/limits.conf',
  provider => 'shell'
}
