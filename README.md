# ContraBot
 ContraBot is an application that aims to provide contradiction detection for speech, both for real time audio and recorded audio files.
 
 Application implements the GiddyUp text-contradiction framework.

## Setup
 If you are cloning the repo for the first time use the following command to clone repo with submodule:

 `git clone --recurse-submodule https://github.com/GiddyUpInc/ContraBot.git`

 Create anaconda environment:

 `conda create -n <name>`

 Install project requirements:
 
 `pip install -r requirements.txt`

## Updating submodules
 To ensure you are using the up to date text analysis tool, use:
 ```
 git submodule init
 git submodule update
 ```
 