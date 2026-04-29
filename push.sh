#!/bin/bash

cd /Users/javi/Desktop/uber_analytics_project || exit

git add .
git commit -m "Auto update: $(date '+%Y-%m-%d %H:%M:%S')" || echo "Nothing 
new to commit"
git push

