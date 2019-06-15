# Lost&Found

A lost and found web server can be used for many use-case

##  Setup and prerequisites

### 1. install Python

Go to Python official website and download latest version of Python https://www.python.org/downloads/

### 2. Setup virtual environment (It's optional but good practice)
**Jump to step 5, if you don't use virtual environment**
```
pip install virtualenv
```

### 3. Create virtual environment in local repository

Open terminal and goto Lost-Found folder, enter following command
```
virtualenv -p python .
```

### 4. Open project in virtual environment
Open terminal and goto */Lost-Found* folder, then activate virtualenv mode
```
./Scripts/activate
```

### 5. Install Modules
```
pip install django-cleanup
```
```
pip install Pillow
```

### 6. Run server
In the terminal, goto */Lost-Found/src* folder, enter following to run server

```
python .\manager.py runserver
```

The server is hosting at *http://127.0.0.1:8000/* by default
