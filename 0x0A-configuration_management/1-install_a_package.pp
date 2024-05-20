# puppet declarative script to install flask from pip3.
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'Werkzeug':
  ensure   => '2.0.3',  # Use a compatible version with Flask 2.1.0
  provider => 'pip3',
}
