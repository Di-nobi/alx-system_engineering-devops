#Executing a kill command
exec {'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
