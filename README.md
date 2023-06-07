


<a name="readme-top"></a>



[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br>
<div align="center">
  <a href="https://github.com/Johnny-FTW/EventAggregationService">
    <img src="https://raw.githubusercontent.com/Johnny-FTW/EventAggregationService/c9abbe3f379be037675f981b6c74c0c6d38a5cc6/EventViewer/static/uniswap.svg" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Event Aggregation Service</h3>

  <p align="center">
    The goal was to create a website that allows organizers 
to enter events and collect entries for them. Any registered 
user can sign up. The website also have events search engine
(with several criteria) and an API, that will allow the presentation on other pages / services.

  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#requirements">Requirements</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## About The Project




Main system features:
* User registration and login.
* Creating and editing events by organizers (user with a special role).
* Commenting on events by a logged in users.
* Signing up for events.
* Events search engine.
* API for other websites / services that want to present events.

### Built With

* [![Python][Python.org]][Python-url]
* [![Django][Django.com]][Django-url]
* [![HTML][HTML.com]][HTML-url]
* [![CSS][CSS.com]][CSS-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]
* [![JS][JS.com]][JS-url]
* [![JQuery][JQuery.com]][JQuery-url]
* [![SQL][SQL.com]][SQL-url]

General Guidelines:
* Website development using Django and Django REST Framework as an API.
* Introducing the division into models, views and controllers in the application and placing the appropriate logic in each of them.
* Securing access to the application and functionality by using django.contrib.auth

Screenshots:

![image](https://raw.githubusercontent.com/Johnny-FTW/EventAggregationService/main/imgs/Screenshot_1.png)
<br>
![image](https://raw.githubusercontent.com/Johnny-FTW/EventAggregationService/main/imgs/Screenshot_2.png)
<br>
![image](https://raw.githubusercontent.com/Johnny-FTW/EventAggregationService/main/imgs/Screenshot_3.png)
<br>
![image](https://raw.githubusercontent.com/Johnny-FTW/EventAggregationService/main/imgs/Screenshot_4.png)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

To get a local copy up and running follow these simple example steps.

### Requirements

List of requirements:
* asgiref==3.6.0
* certifi==2022.12.7
* charset-normalizer==3.0.1
* Django==4.1.6
* djangorestframework==3.14.0
* idna==3.4
* pytz==2022.7.1
* requests==2.28.2
* sqlparse==0.4.3
* tzdata==2022.7
* urllib3==1.26.14
<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Installation

Below is an example of how to install and set up this app.

1. Clone the repo
   ```sh
   git clone https://github.com/Johnny-FTW/EventAggregationService.git
   ```
2. Install project dependencies
   ```sh
   pip install -r requirements.txt
   ```
3. Then simply apply the migrations
   ```sh
   python manage.py migrate
   ```
4. You can now run the development server
   ```sh
   python manage.py runserver
   ```
<p align="right">(<a href="#readme-top">back to top</a>)</p>

## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Contact

- Jan Hatapka - [Linkedin](https://www.linkedin.com/in/jan-hatapka-6b970b205/) - mail: jan.hatapka@gmail.com 
- Michael Klimik

Project Link: [https://github.com/Johnny-FTW/EventAggregationService](https://github.com/Johnny-FTW/EventAggregationService)

<p align="right">(<a href="#readme-top">back to top</a>)</p>




[Python.org]: https://img.shields.io/badge/Python-14354C?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/

[Django.com]: https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white
[Django-url]: https://www.djangoproject.com/

[HTML.com]: https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML-url]: https://https://html.com//

[CSS.com]: https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS-url]: https://www.css3.com/

[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com

[JS.com]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JS-url]: https://www.javascript.com/

[JQuery.com]: https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white
[JQuery-url]: https://jquery.com 

[SQL.com]: https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white
[SQL-url]: https://www.sqlite.org/index.html


[contributors-shield]: https://img.shields.io/github/contributors/Johnny-FTW/EventAggregationService.svg?style=for-the-badge
[contributors-url]: https://github.com/Johnny-FTW/EventAggregationService/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/Johnny-FTW/EventAggregationService.svg?style=for-the-badge
[forks-url]: https://github.com/Johnny-FTW/EventAggregationService/network/members

[stars-shield]: https://img.shields.io/github/stars/Johnny-FTW/EventAggregationService.svg?style=for-the-badge
[stars-url]: https://github.com/Johnny-FTW/EventAggregationService/stargazers

[issues-shield]: https://img.shields.io/github/issues/Johnny-FTW/EventAggregationService.svg?style=for-the-badge
[issues-url]: https://github.com/Johnny-FTW/EventAggregationService/issues

[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/Johnny-FTW/EventAggregationService/blob/main/LICENSE.txt

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/jan-hatapka-6b970b205/