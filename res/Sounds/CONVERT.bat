echo off
ffmpeg -i SAIDi.mp3 -filter:a "atempo=1.2" -vf -vn SAIDo.wav
