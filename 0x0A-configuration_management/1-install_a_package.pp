#!/usr/bin/pup
#installing flask
package {'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
