#!/bin/bash
uwsgi --uid=www-data --gid=www-data -s /tmp/uwsgi.sock --module index --callable app