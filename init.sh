xrandr --newmode "800x480_60.00"   29.50  800 824 896 992  480 483 493 500 -hsync +vsync

xrandr --addmode HDMI-1 800x480_60.00

xrandr --output HDMI-1 --mode 800x480_60.00

python3 src/main.py
