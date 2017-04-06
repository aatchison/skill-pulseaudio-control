# Pulseaudio device control skill

## Description:
This skill is intended to allow a Mycroft user to list and set the default input and output devices. This should work both by voice and by cli for an initial setup.

## Usage:
* `pulse source list`
* `pulse sink list`
* `pulse source set (integer)`
* `pulse sink set (integer)`

## Status:
* `listing devices should work just fine`
* `setting devices speaks the device that was set, but setting hasn't been implemented just yet`
