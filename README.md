#basura-app
The app which reads the data from the basura-trashcan via bluetooth and reports it to basura-server via http.
This is part of the FSE 2018 Trash Can System.

#Installation
The app was developed using [kivy](https://kivy.org/#home) which is an open source library for Python for creating apps. 
The versions used were Kivy v1.10.1 with Python v3.6.7. on Ubuntu 18.04.1.

#Setting up the virtual environment
The virtual environment is set up using the instructions from the kivy webpage which can be found [here](https://kivy.org/doc/stable/installation/installation-linux.html).
    
    % sudo apt-get install -y \
    python-pip \
    build-essential \
    git \
    python3 \
    python3-dev \
    python3-pip \
    ffmpeg \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    libportmidi-dev \
    libswscale-dev \
    libavformat-dev \
    libavcodec-dev \
    zlib1g-dev

Create a virtualenv named "venv"
using the default interpreter:

      % sudo pip3 install virtualenv
      % cd basura-app
      % virtualenv venv -p python3

Activate the virtualenv:
  
      % source venv/bin/activate

Install Cython and kivy

    (venv) % pip install -r requirements.txt
    

Now you can run the kivy based basura-app code locally on your computer or laptop.

#Deploy the App to your Android phone
In order to run the app on your mobile device, an Android APK package is build.
We follow the online documentation provided by kivy to [create a package for Android](https://kivy.org/doc/stable/guide/packaging-android.html).

The Buildozer tool automates the whole python to android process (not supported on Windows). It can be downloaded
from the Kivy GitHub page. In your virtual environment follow the [instructions](https://pypi.org/project/buildozer/) 
for installing *buildozer* for python 3:
 
      (venv) % sudo pip install buildozer
 
In the project directory:

       (venv) % buildozer init

The last command creates the *buildozer.spec* file which needs to be customized as it controls the build configuration.
It should be edited with the app name etc. and variables to control most or all of the parameters passed to python-for-android.

The NDK zip file was previously download [here](https://developer.android.com/ndk/downloads/). Please unzip it

        (venv) % unzip android-ndk-r19-linux-x86_64.zip
        
Further installations needed:

        (venv) % sudo apt-get install -y autoconf automake libtool
      
and write the path into the *buildozer.spec* file under *android.ndk_path = your_path_here/android-ndk-r19*.

Then plug in your android device and run:

       (venv) % buildozer android debug deploy run

In order to exit the virtual environment type:
       (venv) % deactivate

#Error
[INFO]:    No existing dists meet the given requirements!
[INFO]:    No dist exists that meets your requirements, so one will be built.
[ERROR]:   Didn't find any valid dependency graphs.
[ERROR]:   This means that some of your requirements pull in conflicting dependencies.
[ERROR]:   Exiting.
Command failed: /usr/bin/python3 -m pythonforandroid.toolchain create --dist_name=basuraapp --bootstrap=sdl2 --requirements=python3,kivy,python3-pip,python3-dev --ndk-api 9 --arch armeabi-v7a --copy-libs --color=always --storage-dir="/home/happycarmi/FSE/basura/basura-app/.buildozer/android/platform/build"
 
Buildozer failed to execute the last command
The error might be hidden in the log above this error
Please read the full log, and search for it before
raising an issue with buildozer itself.
In case of a bug report, please add a full log with log_level = 2
