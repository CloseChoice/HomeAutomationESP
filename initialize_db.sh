#!/bin/bash

if [ -f "database/temperature_humidity.db" ]; then
    rm "database/temperature_humidity.db"
    echo "deleted database/temperature_humidity"
fi
python database/init_db.py