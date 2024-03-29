# add a custom HTTP header X-Served-By

exec {'get_updates':
  command => '/usr/bin/apt-get update',
}

package {'nginx':
  ensure  => 'installed',
  require => Exec['get_updates'],
}

$custom_header = "add_header X-Served-By \"${hostname}\";"

exec {'add_custom_header':
command  => "echo '${custom_header}' | sudo sed -i '50r /dev/stdin' /etc/nginx/sites-enabled/default",
provider => 'shell',
}

service {'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}