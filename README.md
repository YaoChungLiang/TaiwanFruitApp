# TaiwanFruitsApp

## Introduction
This app aims to help local farmers and market seller to sell their fruits in Taiwan.
During the economy recession, lots of people aren't being able to get outside. 
Let's figure a way out to help soothe the pain not being able to going outside but still can get some fruits.

## link
`${Todo link}`

## Developer Usage
Structure of the repo is below
```bash
root
   |--.gitignore
   |--src/Taiwna/
        |--Taiwan/         (project)
        |--TaiwanFruits/   (app)
        |--pages/          (app)
        |--templates/      (html templates)
        |--uploads/        (client image, pdf data)
        |--db.sqlite3      (relational database)
        |--manage.py
```

1. Clone the repo by typing the command below on your terminal.\
`git clone https://github.com/YaoChungLiang/TaiwanFruitApp/tree/windows_linux/src/Taiwan`
2. Install the software requirements in your computer\
`pip install -r requirements.txt`
3. Run the app by going to the directory src/Taiwan/ and run the command below\
`python manage.py runserver`
4. Open your web browser and go to the internal network by typing the url on your screen,\
Starting the development server at `${url you need to type into your browser}`
by default it's `127.0.0.1:8000` (loopback Ipv4 address:port number)\

## Requirements
python >= 3.5.x\
django >= 2.1.5

## Memo
Check what you want to do to the app by typing the command below\
`python manage.py -h`

## License
MIT

