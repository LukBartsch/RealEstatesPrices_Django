
# Real Estates Prices Monitor - Django
Web application for monitoring real estates prices. You can see [_here_](#).


## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Main View](#main-view)
* [Setup](#setup)
* [Project Status](#project-status)
* [Contributing](#contributing)
* [Contact](#contact)
* [License](#license)


## General Information
The application is used to monitor real estate prices for two selected cities and for two types of markets (primary and secondary market).

Application built using the Django framework.

The application uses market data stored in a MySQL database.

The database also stores historical data on real estates prices (since 2006) which can be displayed on a chart along with the most recent data.


## Technologies Used
* [Django](https://fastapi.tiangolo.com/)
* [SQLAlchemy](https://www.sqlalchemy.org/)


## Main View

The application is a single-page website where the user can select the city, market type and data type. The Chart.js library was used to generate line charts.

![image](https://github.com/user-attachments/assets/9cb71dbc-27bc-4cb2-be77-4e289ce708b4)



Below the graph there is also information in a table about the current average prices of apartments per square meter. And information about the average area or number of rooms.

![image](https://github.com/user-attachments/assets/a7e46b18-5a64-4711-bd0b-979b88d09b9e)



## Setup
- Clone repository
* Rename .env.example to `.env` and set your value
```
SECRET_KEY=<some_random_string>
DB_NAME=<your_db_name>
DB_USER=<your_db_username>
DB_PASSWORD=<your_db_password>
DB_HOST=<your_db_host>
```

* Install packages from `requirements.txt`
```
pip install -r requirements.txt
```
* Run Django application
```
cd main
python manage.py runserver
```

* The application will be available at the local address: 
```
http://127.0.0.1:8000/
```

## Project Status
Application made in trial version for the purpose of learning Django framework.


## Contributing
If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement". I will be very grateful for any interesting ideas.


## Contact
Created by [@LukBartsch](https://github.com/LukBartsch) - feel free to contact me!

[![LinkedIn][github-shield]][github-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


## License
This project is open source and available under the MIT License.


[github-shield]: https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white
[github-url]: https://github.com/LukBartsch
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/lukasz-bartsch/


