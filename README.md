#basura-app

The app which reads the data from the basura-trashcan via bluetooth and reports it to basura-server via http.
This is part of the FSE 2018 Trash Can System.

#Installation
The app was developed using [kivy](https://kivy.org/#home) which is an open source library for Python for creating apps. 
The versions used were Kivy v1.10.1 with Python v3.6.7.

#Setting up the virtual environment
The virtual environment is set up using the instructions from the kivy webpage which can be found [here](https://kivy.org/doc/stable/installation/installation-linux.html).
    
    %sudo apt-get install -y \
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

Make sure Pip, Virtualenv and Setuptools are updated

    %sudo pip3 install --upgrade pip virtualenv setuptools

Then create a virtualenv named "venv"
using the default interpreter:

    % virtualenv --no-site-packages venv

Enter the virtualenv:

    % . venv/bin/activate

Install Cython and kivy

    %pip3 install Cython==0.29.2
    %pip3 install kivy

#Exporting the App to your Android phone
For this we need the buildozer.

#Usage
Happy Usage!