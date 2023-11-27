# fixing issues
exec { 'Corrections-1':
  command  => 'sudo sed -i \ 's/nofile 5/nofile 30000/\' /etc/security/limits.conf',
  provider => shell,

}

exec { 'Corrections-2':
  command  => 'sudo sed -i \ 's/nofile 4/nofile 10000/\' /etc/security/limits.conf',
  provider => shell,

}
