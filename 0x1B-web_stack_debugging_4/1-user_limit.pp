file_line { 'set_holberton_hard_limit':
  ensure  => present,
  path    => '/etc/security/limits.conf',
  line    => 'holberton hard nofile 5000',
  match   => '.*holberton hard nofile.*',
}

file_line { 'set_holberton_soft_limit':
  ensure  => present,
  path    => '/etc/security/limits.conf',
  line    => 'holberton soft nofile 4000',
  match   => '.*holberton soft nofile.*',
}
