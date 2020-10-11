# Using Klio to Scale and Share Your Research - Pre-Work

Hello and welcome to our tutorial on Klio! 

## Assumptions
In this tutorial, we assume that: 

* You are comfortable coding in the Python programming language. 
* You have access to  a Unix-based environment
* You are comfortable working in a terminal application with a Unix-based shell, e.g. bash, zsh, etc.

We will be running commands in a shell environment inside a Docker container and editing code. 

In order for the tutorial to run smoothly, we will need you to follow the steps below on the computer that you are planning to run the tutorial in.
System Requirements
* Docker (instructions [here](https://docs.docker.com/get-docker/) to install) 
* git (instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) to install)
* A code editor (we suggest [Sublime Text](https://www.sublimetext.com/3))

> **_Why Docker?_** In order to ensure that all attendees of the tutorial are working with the same environment, we've created a Docker image with klio pre-installed in it. If you're not familiar with Docker, a tool for running identical, isolated environments across many computers, you can learn more about it [here](https://docs.docker.com/get-started/). 



### Step 1: Download the code example and data


*Either* clone it from this repository:

```
git clone https://github.com/fallonchen/ismir-klio.git
```

*Or* 

Download the zip file from this repository by clicking on the green Code button and select "Download ZIP".

 

After cloning/downloading the code, inside the code example you should see the following:

```
launch-klio-tutorial.sh
changed_files/
pitch_tracker/
pitch-tracker-job-output/
```

The `pitch_tracker/` directory contains example code that you will use during the tutorial. 

The `changed_files/` will provide a reference for working code, if you need it. 

The `pitch-tracker-job-output/` directory is currently empty, and will be used to hold the output of your job.

### Step 2: Confirm that the your setup works
In a terminal, navigate to the directory with the example code and run:

```
$ ./launch-klio-playground.sh
```

This script downloads the prepared Docker image, and launches the container in interactive mode with Klio installed for you inside of it. Once finished, your terminal should show something like this:

```
root@1ee87cb4f3cc#
```

And you should be able to run the klio command and see its help text:

```
root@1ee87cb4f3cc# klio
Usage: klio [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  image    Manage a job's Docker image.
  job      Create and manage Klio jobs.
  message  Manage a job's message queue via Pub/Sub.
```

If you are having trouble with this step, please ping us on Slack! 

If you have access to the ISMIR 2020 slack, you can find us in the [#tutorial-1-klio-tutorial](https://app.slack.com/client/T01AAT8RPMZ/C01C2MY697W/details/actions) room. 

If you don't yet have access to the ISMIR 2020 slack, you can sign up for the [Spotify FOSS Slack](https://slackin.spotify.com/) and ping us in the [#klio](https://spotify-foss.slack.com/archives/C0177KD51AP) channel.


And that's it! You're ready to go. 🙌

## After the Tutorial

Klio is [released](https://github.com/spotify/klio) under the Apache 2.0 license. Documentation is on [Read the Docs](https://klio.readthedocs.io) and how to setup on your local machine can be found [here](https://klio.readthedocs.io/en/latest/quickstart/index.html).
