# creating a file /tmp/school
file { '/tmp/school':
  ensure  => 'file',
  content => 'I love puppet',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
}
