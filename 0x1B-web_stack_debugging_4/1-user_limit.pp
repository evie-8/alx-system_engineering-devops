# fixing login errors 
exec { 'Corrections-1':
  command => 'sudo sed -i "/holberton hard/s/5/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'

}

exec { 'soft-file-limit-increase':
  command => 'sudo sed -i "/holberton soft/s/4/50000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/',

}
