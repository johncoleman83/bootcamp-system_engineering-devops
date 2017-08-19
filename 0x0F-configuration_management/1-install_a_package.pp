# puppet manifest to install puppet-lint package with gem
package { 'puppet-lint':
  ensure   => '1.1.0',
  provider => 'gem',
}
