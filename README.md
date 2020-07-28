# Introducing...

<p align="center">
  <img src="https://raw.githubusercontent.com/jonathankamau/note-taking-app/master/app/data/noteworthy.gif"/>
</p>

## An open-source simple Note Taking App built with Django that allows you to make meeting notes conveniently and efficiently. 

## It can be accessed LIVE here: https://noteworthy-2020.herokuapp.com/

# Technologies Used
### Python 3.7.8
### Django 3.0.8

# Installation

1. create a working directory

	      $ mkdir -p work-dir
	      $ cd workdir


2. clone this repo to local
    - Via SSH

          	git clone git@github.com:jonathankamau/note-taking-app.git

    - via HTTPS

          	git clone https://github.com/jonathankamau/note-taking-app.git
          
3. Navigate to project directory
    
    
      		$ cd note-taking-app
      		$ cd checkout -b <new branch>

4. Download and Install PostgreSQL if you haven't already following the directions outlined [here](https://www.postgresql.org/download/) for your OS

5. Install Postico which is a PostgreSQL client and use it to create a new database. Alternatively you can use the PostgreSQL terminal to create one.

6. Run migrations through the following commands. Ensure you are running them with Python 3.7.8:

            $ python manage.py makemigrations
            $ python manage.py migrate

7. Load fixtures to the MeetingCategory table by running:

            $ python manage.py loaddata app/data/categories.json 

8. Start the server by running:

            $ python manage.py runserver

9. On your browser, navigate to http://127.0.0.1:8000/ and you should be able to see the app running

## Authors

* **Jonathan Kamau** - [Github Profile](https://github.com/jonathankamau)


## License

This project is licensed under the MIT License.


