#!/bin/bash

# update local repositories
git pull

# add dir to local repositories
git add .

# update commit
read -p "Input the update commit:" update_commit

git commit -m "${update_commit}"

# push local repositories to remote
git push -u origin main
