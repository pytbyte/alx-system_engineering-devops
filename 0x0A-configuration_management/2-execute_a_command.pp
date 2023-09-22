# Puppet Manifest to kill a process by its name using exec
exec { 'killmenow':
  command     => 'pkill killmenow',
  path        => '/bin/',
  refreshonly => true,
  onlyif      => 'pgrep killmenow',
}
