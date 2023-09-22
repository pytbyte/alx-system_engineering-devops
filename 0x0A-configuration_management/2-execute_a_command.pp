# Puppet Manifest to kill a process by its name using exec
exec { 'pkill killmenow' :
    path    => '/bin/',
    command => 'pkill killmenow',
    }
