#!/bin/sh

python create_tables.py

exec fastapi run main.py