#works. Compile requests and python3 modules for android
#install python modules in python-for-android virtual environment
#rebuild with dystopia app specifications
#install requests with command $pip install requests | activate venv at  cd /home/samuel/.local/share/python-for-android/build/venv/bin && source activate
#godot python uses python3.8
#generate godot python bindings
./p4a apk --private /home/samuel/webserver/client_requests.py --package=org.example.myapp --name "Hallo World" --version 0.1 --bootrstrap=sd12 --requirements=python3.7,requests --sdk_dir /home/samuel/Android/Sdk/ --ndk_dir /home/samuel/Android/Sdk/ndk/24.0.8215888/ --android_api 30 --ndk_version 24.0.8215888 --arch=armeabi-v7a

