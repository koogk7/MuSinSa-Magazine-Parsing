## Musinsa Magazine Crawler

### ScreenShot
![Screen Shot](https://user-images.githubusercontent.com/48513360/59121173-55400400-8992-11e9-9cc9-a2695079ff94.png)

### Evironment 
- Python         3.7.2
- beautifulsoup4 4.7.1  
- pip            19.0.3  
- PyMySQL        0.9.3  
- requests       2.22.0 
- target url : https://www.musinsa.com/index.php?m=magazine

### How to use
1. First, you must start virtual environment. Typing below command in your project terminal.
    ```shell
    source venv/bin/activate
    ```
2. You must create a table named 'musinsa' in your database. This schema is above image in screenshot session.

3. This part of code to relate databse is empty. So you should complete this part to run this code. The place to write is 'constant.py'
    ```python
    MUSINSA_URL = "https://www.musinsa.com/"
    MAGAZINE_URL = "?m=magazine"
    DATABASE_ENDPOINT = ""
    DATABASE_NAME = ""
    DATABASE_USER = ""
    DATABASE_PASSWORD = ""
    ```

4. Run 'musinsa_main.py' in your project 

