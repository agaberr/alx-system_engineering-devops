#!/usr/bin/env bash
# Automating ssh authentication using Puppet

file { '/etc/ssh/ssh_config':
  ensure  => present,
content => "
    Host *
      IdentityFile ~/.ssh/school
      PasswordAuthentication no
  ",
}
