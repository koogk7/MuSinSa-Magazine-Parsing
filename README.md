## Musinsa Magazine crawler

### ScrennShot


### Evironment 
- Python         3.7.2
- beautifulsoup4 4.7.1  
- pip            19.0.3  
- PyMySQL        0.9.3  
- requests       2.22.0 
- target url : https://www.musinsa.com/index.php?m=magazine

### How to use
1. First, you must start virtual environment. Typing below command in your project terminal
    ```shell
    source venv/bin/activate
    ```
2. You must create a table named 'musinsa' in your database. This schema is below img.
![Database Schema](https://ibb.co/3YmXtFR)

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

