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

Make sure Pip, Virtualenv and Setuptools are updated

    % sudo pip3 install --upgrade pip virtualenv setuptools

Then create a virtualenv named "venv"
using the default interpreter:

    % virtualenv --no-site-packages venv

Enter the virtualenv:

    % . venv/bin/activate

Install Cython and kivy

    % pip3 install Cython==0.29.2
    % pip3 install kivy

Now you can run the kivy based basura-app code locally on your computer or laptop.

#Deploy the App to your Android phone
In order to run the app on your mobile device, an Android APK package is build.
We follow the online documentation provided by kivy to [create a package for Android](https://kivy.org/doc/stable/guide/packaging-android.html).

The Buildozer tool automates the whole python to android process (not supported on Windows). It can be downloaded
from the Kivy GitHub page. In your virtual environment:
 
    % git clone https://github.com/kivy/buildozer.git
    % cd buildozer
    % sudo python3.6 setup.py install
    % buildozer init

The last command creates the *buildozer.spec* file which needs to be customized as it controls the build configuration.
It should be edited with the app name etc. and variables to control most or all of the parameters passed to python-for-android.


Install buildozer’s dependencies.

    % sudo dpkg --add-architecture i386
    % sudo apt-get update
    % sudo apt-get install build-essential ccache git libncurses5:i386 libstdc++6:i386 libgtk2.0-0:i386 libpangox-1.0-0:i386 libpangoxft-1.0-0:i386 libidn11:i386 python2.7 python2.7-dev openjdk-8-jdk unzip zlib1g-dev zlib1g:i386

Then plug in your android device and run:

    % buildozer android debug deploy run
    
Had the error:

 *Cwd None*
 
*Could not install packages due to an EnvironmentError: [Errno 20] Not a directory: '/usr/lib/python3.6/site-packages/appdirs.py'*

*Command failed: /usr/bin/python3.6 -m pip install -q  'appdirs' 'colorama>=0.3.3' 'jinja2' 'six'* 

Following packages had to be installed:
    % python3.6 -m pip install 'appdirs', 'colorama>=0.3.3', 'sh>=1.10,<1.12.5', 'jinja2', 'six'
    % python3.6 -m pip install virtualenv
    % python3.6 -m pip install pexpect


Please note that the Buildozer Python3 support is only experimental. 

#Have Fun!