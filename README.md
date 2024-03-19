# Voice Search

This project is a web application designed to provide voice search functionality for searching C programs. By utilizing Google's Speech-to-Text API, users can navigate and explore C programs using voice commands, enhancing productivity and saving time.


### Home Screen
![Home Page](https://github.com/quirrelHK/voice-search/blob/master/media/home_screen.png)

### Results after voice search:
_c program to add 2 numbers_
![Results](https://github.com/quirrelHK/voice-search/blob/master/media/output.png)

### High level overview
![Overview](https://github.com/quirrelHK/voice-search/blob/master/media/flow_diagram.png)

## Features
- **Voice Search:** Users can search for C programs using voice commands.
- **Real-time Speed Search:** The application provides real-time search functionality to quickly find relevant C programs.
- **Productivity Enhancement:** By enabling voice-based navigation, this tool aims to maximize productivity for developers and programmers.


## How to run the app
1. Clone the repository and cd into the directory
```console
git clone https://github.com/quirrelHK/voice-search.git
```
2. Running a virtual environment is recommended, in command prompt:
```console
python -m venv base
base\Scripts\activate.bat
```
3. Install the requirements using pip
```console
pip install -r requirements.txt
```
4. Run the app
```console
flask --app app run --debug
```