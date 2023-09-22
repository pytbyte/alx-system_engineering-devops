# Puppet Manifest to kill a process by its name using exec
exec {'terminate_killmenow':
    command     => 'pkill killmenow',
    refreshonly => true,
    onlyif      => 'pgrep killmenow',
}
