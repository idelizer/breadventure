![wheat](https://github.com/idelizer/bread-journal-project/blob/main/static/img/wheat.jpg)

# Breadventure

Visit Breadventure [here](https://breadventure.herokuapp.com/) to start your journey!

Breadventure is a webapp for tracking experiments with bread making and sourdough starters.

Users can create an account, then log in to record recipes they have tried, inputting all the different details they may want to track. 
See your progress as bread maker looking back over your recipes!

<p align="center">
  <br>
  <img src="https://github.com/idelizer/bread-journal-project/blob/main/static/img/screenshots/home.png" width="90%"/>
  <br>
  <br>
  <img src="https://github.com/idelizer/bread-journal-project/blob/main/static/img/screenshots/user.png" width="90%"/>
</p>

## See the ingredients and instructions you recorded about your experiment!

Any input you added is displayed in an easy-to-read format. These details can include ingredients, the temperature baked at, a photo of your bread, and more!
Ingredients are in displayed grams, as well as in a graph of dynamically generated baker's percentages.

<p align="center">
  <br>
  <img src="https://github.com/idelizer/bread-journal-project/blob/main/static/img/screenshots/details.png" width="90%"/>
  <br>
  <br>
  <img src="https://github.com/idelizer/bread-journal-project/blob/main/static/img/screenshots/graph.png" width="90%"/>
</p>

## Stack
* Python
* JavaScript
* PostgreSQL
* HTML
* CSS
* Flask
* Jinja
* Bootstrap 
* SQLAlchemy 
* Chart.js
* Heroku

## APIs
* [Cloudinary](https://cloudinary.com/documentation)
* [Spoonacular](https://spoonacular.com/food-api)

<p align="center">
  Built as a capstone project for Hackbright Academy. Deployed August 16, 2021.
  <br>
  <br>
  <img src="https://github.com/idelizer/bread-journal-project/blob/main/static/img/logo.jpg" width="100"/>
</p>

## 1. Clone repository

  ```
  cd <directory>
  git clone https://github.com/idelizer/bread-journal-project.git
  ```
    
## 2. Download prerequisites

  ### 1. Python 3.7.0 or later
  Check your version of Python with `python --version` or download Python [here](https://www.python.org/downloads/).
    
  ### 2. Set up a virtual environment using venv
  To create a virtual enviroment using venv, run
  ```
  python3 -m venv .venv
  ```
  To run virtual environment, run
  ```
  source .venv/bin/activate
  ```
  To deactivate virtual environment when finished using it, run
  ```
  deactivate
  ```
  You can find documentation on venv [here](https://docs.python.org/3/library/venv.html) as well as Virtual Environments and Packages [here](https://docs.python.org/3/tutorial/venv.html).
  You can use other virtual enviroments such as [pipenv](https://pipenv.pypa.io/en/latest/install/) or [poetry](https://python-poetry.org/docs/managing-environments/) with minor tweaking. 
  
  ### 3. Import configuration file and install packages 
  While running the virtual environment, run
  ```
  pip install -r requirements.txt
  ```
    
## 3. Run in browser
While running the virtual enviroment, run
```
python3 server.py
```

> Note about error `[Errno 48] Address already in use`: This application uses Port 5000. You can change port of use in bread-journal-project/server.py.
> ```
> if __name__ == '__main__':
>     app.run(host='0.0.0.0', port=os.environ.get("PORT", "5000"), debug=True)
> ```
> Or if using MacOS, disable Airplay, as it uses port 5000.
>> Settings > General > AirDrop & Handoff > toggle AirPlay receiver
