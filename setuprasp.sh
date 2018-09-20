echo "Passo 1/5"
# sudo apt-get update -y

echo "Passo 2/5"
sudo apt-get install libsdl2-dev -y
sudo apt-get install libsdl2-image-dev -y
sudo apt-get install libsdl2-mixer-dev -y
sudo apt-get install libsdl2-ttf-dev -y
sudo apt-get install pkg-config -y
sudo apt-get install libgl1-mesa-dev -y
sudo apt-get install libgles2-mesa-dev -y
sudo apt-get install python-setuptools -y
sudo apt-get install libgstreamer1.0-dev -y
sudo apt-get install git-core -y
sudo apt-get install gstreamer1.0-plugins-{bad,base,good,ugly} -y
sudo apt-get install gstreamer1.0-{omx,alsa} -y
sudo apt-get install python-dev -y
sudo apt-get install libmtdev-dev -y
sudo apt-get install xclip -y
sudo apt-get install xsel -y

echo "Passo 3/5"
#sudo apt-get install cython
sudo pip3 install Cython

echo "Passo 4/5"
sudo pip3 install git+https://github.com/kivy/kivy.git@master

#echo "Passo 5/5"
#pip3 install pyaudio 
