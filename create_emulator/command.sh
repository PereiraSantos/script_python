#!/usr/bin/env bash

path='/home/user/script/create_emulator'
find='[system]+[-]+[images]+[;]+[android]+[-]+([0-9]{1,})+[;][a-z]+[;]+[x]+[0-9]{1,}'

if [ $1 = 1 ]; then
	sdkmanager --list > $path/list.txt
    cat $path/list.txt | grep -E -i $find > $path/list_android.txt
elif [ $1 = 2 ]; then
    sdkmanager "platforms;$4"
    sdkmanager "$3;$4;$5;$6"
	avdmanager --silent create avd -n $2 -k "$3;$4;$5;$6"
elif [ $1 = 3 ]; then
	emulator -list-avds > $path/emulator.txt
elif [ $1 = 4 ]; then
	avdmanager delete avd -n $2
fi
