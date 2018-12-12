## Follow the below steps to set up this project

1. Clone the repository:
```cmd
git clone https://github.com/azmeerhosen/assignment.git
```

2. Enter into the project repo:
```cmd
cd assignment
```

3. Make sure that you have Python >= 3.5 installed in your system.

4. Create virtual environment:
```cmd
virtualenv -p python3 venv
```
If you don't have `virtualenv` installed, install it using `pip`:
```cmd
pip install virtualenv
```

5. Activate virtualenv:
If your system is `Linux`, then use following command
```cmd
source venv/bin/activate
```
For `windows`
```cmd
venv\Scripts\activate
```

6. Install dependencies:
```cmd
pip install -r requirements.txt
```

7. Create Databasae tables:
```cmd
python3 manage.py makemigrations
python3 manage.py migrate
```
If these commands don't work, then use
```cmd
python3 manage.py makemigrations photo_sharing
python3 manage.py migrate photo_sharing
```

8. Create Superuser:
```cmd
python3 manage.py createsuperuser
```
Enter all the credentials when it prompts.

9. Now, run the development server:
```cmd
python3 manage.py runserver
```
Enter in your browser's address bar the ip with port shown in terminal/console.




