# using a puppet script to create ssh config file

file_line { 'identity':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config'
  line   => '	IdentityFile ~/.ssh/school',
}

file_line { 'password':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '	PasswordAuthentication no',
}
