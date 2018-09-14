echo "Passo 1/5"
sudo apt-get update

echo "Passo 2/5"
sudo apt-get install libsdl2-dev
sudo apt-get install libsdl2-image-dev
sudo apt-get install libsdl2-mixer-dev
sudo apt-get install libsdl2-ttf-dev
sudo apt-get install pkg-config
sudo apt-get install libgl1-mesa-dev
sudo apt-get install libgles2-mesa-dev
sudo apt-get install python-setuptools
sudo apt-get install libgstreamer1.0-dev
sudo apt-get install git-core
sudo apt-get install gstreamer1.0-plugins-{bad,base,good,ugly}
sudo apt-get install gstreamer1.0-{omx,alsa}
sudo apt-get install python-dev
sudo apt-get install libmtdev-dev
sudo apt-get install xclip
sudo apt-get install xsel

echo "Passo 3/5"
sudo pip3 install -U Cython==0.28.2

echo "Passo 4/5"
sudo pip install git+https://github.com/kivy/kivy.git@master

echo "Passo 5/5"
pip3 install pyaudio 

