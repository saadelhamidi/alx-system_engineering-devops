#!/usr/bin/env bash
# puppet_ssh_config.pp

class ssh_config {
  file_line { 'Turn off passwd auth':
    path   => '/etc/ssh/ssh_config',
    line   => 'PasswordAuthentication no',
    match  => '^#?PasswordAuthentication',
  }

  file_line { 'Declare identity file':
    path   => '/etc/ssh/ssh_config',
    line   => '    IdentityFile ~/.ssh/school',
    match  => '^#?IdentityFile',
  }
}
include ssh_config
