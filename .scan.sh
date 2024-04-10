#!/bin/bash

brew install ruby brew-gem
brew gem install cfn-nag

cfn_nag_scan --input path template.yaml

# pip install bandit

# bandit test_code.py