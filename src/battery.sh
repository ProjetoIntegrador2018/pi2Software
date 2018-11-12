upower -i $(upower -e | grep BAT) | grep -E percentage | xargs | cut -d' ' -f2|sed s/%// > /tmp/.batteryPercentage
upower -i $(upower -e | grep BAT) | grep -E state | xargs | cut -d' ' -f2|sed s/%// > /tmp/.batteryState
cat /tmp/.batteryPercentage

exit 0
