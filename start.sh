#!/bin/sh
cd /opt/app
python model.py
gunicorn -b 0.0.0.0:8000 app