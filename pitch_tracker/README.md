# ismir-2020-tutorial-example
Repo that ISMIR 2020 attendees will clone

This tutorial begins with a batch Klio pipeline that takes .wav files, and uses the [MARL crepe
 model](https://github.com/marl/crepe) to track the pitch of the audio files and output a CSV
  file of time, frequency, and confidence. Sample vocal data taken from [Zenodo](https://zenodo.org/record/1442513#.X1p27JNKgdV)

## TUTORIAL PHASES

The first part of the tutorial will cover getting this batch Klio job running locally on a
 DirectRunner using downloaded files stored on your computer.

The second part of this tutorial will convert the batch job into a streaming Klio job, again
 running locally.

After the above hands on part of the tutorial, we will demonstrate how to scale the audio
 processing job to handle a much higher throughput and run on GCP and Dataflow workers.
 
## Quick Links

* [MARL crepe model](https://github.com/marl/crepe)
* [Klio Documentation]()
* [Provided Audio Files](https://zenodo.org/record/1442513#.X1p27JNKgdV)

## Citations

Wilkins, Julia, Prem Seetharaman, Alison Wahl, & Bryan Pardo. (2018).
VocalSet: A Singing Voice Dataset (Version 1.2) [Data set]. Zenodo.
http://doi.org/10.5281/zenodo.1442513