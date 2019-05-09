# Logging to StackDriver

## syslog
syslog -> [ fluentd ] -> stackdriver
fluentd = fluentd syslog input plugin -> stackdriver output plugin

fluentd has a syslog input plugin to listen on a configured port

the stackdriver output plugin requires local secrets: auth for a gcp service account with access to write to stackdriver logging

## unified logging
log command tail -> fluentd -> stackdriver

unified logging stores logs in memory and a binary format created by apple, "tracev3", and the tools to read these files are apple's log command or gui app Console.

### details
* Overview for devs:
http://krypted.com/mac-os-x/logs-logging-logger-oh/

* Source for logging actions:
https://github.com/apple/darwin-xnu/blob/master/libkern/os/log.c
