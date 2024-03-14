# Quorum Coding Challenge: Legislative Data

This repository contains the solution for the Quorum Coding Challenge: Legislative Data.

To see the questions and the answers, please check the [QUESTIONS.md](QUESTIONS.md) file.

<h4 align="left"> 
	Authors :pencil2:
</h4>

<p align="left">
 <a href="https://github.com/maycolteles">Maycol Teles Costa Dionisio Pereira</a> 
</p>

*********************

## Summary :clipboard:

* [Requirements](#requirements)
* [Setup and Installation](#setup-installation)
* [How to Use](#how-to-use)
* [Technical Information](#technical-information)
* [Final Considerations](#final-considerations)

*********************

##  Requirements :pencil: <a name="requirements"></a>

* [Python 3.10+](https://www.python.org/)
* Pip 23.0+ (comes with Python 3)

*********************

##  Setup and Installation :white_check_mark: <a name="setup-installation"></a>

### Cloning the repo :file_folder:
First off, in order to get a copy of the project to run/test it, clone the repository into a folder on your machine:

```
git clone git@github.com:MaycolTeles/quorum.git
```


### Creating and Activating the Virtual Environment :open_file_folder:
It is recommended to install the dependencies inside a [virtualenv](https://docs.python.org/3/tutorial/venv.html). So, inside the folder where you cloned the repository, create a new virtualenv:

```
python3 -m virtualenv venv
```

If you don't have the virtualenv package installed, you can install it with pip:

```
pip install virtualenv
```
    
Now, activate the virtualenv (for Linux/MacOS):

```
source venv/bin/activate
```

or (for Windows):

```
.\venv\Scripts\activate
```

### Installing Dependencies :wrench:
To install all the necessary project dependencies, run the following command in the terminal (make sure you're running it from whithin your virtualenv):

```
pip install -r requirements.txt
```

*********************

## How To Use :man_technologist: <a name="how-to-use"></a>

### Importing the Data :inbox_tray:
To import the data, you just need to run the following command in bash at the same level as `manage.py` file:

```bash
./manage.py import_data_from_csv
```

This command will read all the csv files and create the models in the database.

### Executing the Project :arrow_forward:
To run the application, you just need to run the following command in bash at the same level as `manage.py` file:

```
./manage.py runserver
```

*********************

## Final Considerations :pushpin: <a name="final-considerations"></a>

I changed the `sponsor_id` from `400100` to `412211` in the last line of `bills.csv` as the first `sponsor_id` was not present in `legislators.csv` file.

I wasn't sure if that was expected or not, if it was we can change the code to avoid having to change the CSV file. If it wasn't, we can keep it as it is.