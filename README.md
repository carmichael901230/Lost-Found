# Lost&Found

A lost and found web server can be used for many use-case

# Quick Demo:

### - Home page
![home](https://user-images.githubusercontent.com/34822412/59555691-4524b780-8f84-11e9-9fb5-1f01dc79cdfa.jpg)

### - Register when an item was found
![register](https://user-images.githubusercontent.com/34822412/59555700-700f0b80-8f84-11e9-8c7e-d798a2a8456e.jpg)

### - Search for an item
![search](https://user-images.githubusercontent.com/34822412/59555705-7ac9a080-8f84-11e9-87c4-f094cf2ed2b2.jpg)

### - Edit saved item
![edit](https://user-images.githubusercontent.com/34822412/59555710-8917bc80-8f84-11e9-9d05-8ff0e21b9299.jpg)

#  Setup and prerequisites:

### 1. install Python

Go to Python official website and download latest version of Python https://www.python.org/downloads/

**(Jump to step 5, if you are not going to use virtual environment)**

### 2. Setup virtual environment (It's optional but good practice)

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
