# Cafe Service

## Description
Cafe service, created specifically for Crêpes & Co cafe, helps chefs with management.

### Each chef can: 
- hire new chef, update years of experience, remove chefs who are no longer working,
- add new sections to the menu, edit section names, remove irrelevant sections,
- come up with new dishes on the menu, edit dishes, remove irrelevant positions.

## Check it
[Cafe Service project deployed to Render](https://cafe-service-zvqh.onrender.com/)

#### Test user:
- username: admin.user
- password: admin12345

![DB structure](https://i.ibb.co/yQJQT6Q/drawio-3.png)

## How to run the project
1) Open the command prompt/terminal on your machine.

2) Navigate to the project folder where you want to clone the repository
    ```
    cd /path/to/project
    ```
   
3) Clone project from GitHub.
    ```
    git clone <URL of GitHub repository>
    ```

4) Navigate to the project directory.
    ```
    cd <project directory>
    ```
   
5) Create a virtual environment.
    ```
    python -m venv venv
    ```
     
6) Activate the virtual environment.
   - Unix/Linux/macOS
      ```
      source venv/bin/activate
      ```
   - Windows
      ```
      .\venv\Scripts\activate
      ```
     
7) Install the requirements.
    ```
    pip install -r requirements.txt
    ```
   
8) Сreate a .env file with your parameters as a .env.sample file.
    
9) Run migrations. 
    ```
    python manage.py migrate
    ```  
   
10) Load prepared data from fixture.
    ```
    python manage.py loaddata cafe_service_db_data.json
    ```

11) Run the Django server.
    ```
    python manage.py runserver
    ```
