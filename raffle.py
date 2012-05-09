#!/usr/bin/env python
from random import choice
from github2.client import Github


github = Github()
repos = github.repos.network('github/pycon2011')

print 'And the winners are...'
print '*drumroll*'
print '{0:s} and {1:s}!'.format(choice(repos)['owner'], choice(repos)['owner'])

