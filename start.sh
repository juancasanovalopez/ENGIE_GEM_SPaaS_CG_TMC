#!/usr/bin/env bash
service nginx start
uwsgi --socket 0.0.0.0:8888 --protocol=http -w wsgi:app