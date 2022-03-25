# Steps for run scripts 

*You need to create a .env file in the current dir for database connection*
```
C: src/scripts/ingestions/.env
```
**Inside .env - example**
```
DATABASE_HOST=localhost
DATABASE_USER=root
DATABASE_NAME=Creditoo
DATABASE_PASSWORD=root
DATABASE_PORT=5432
```



**Run in this order**
1. `python src/scripts/ingestions/__alter__.py`
2. `python src/scripts/ingestions/__clients__.py`
3. `python src/scripts/ingestions/__persons__.py`
4. `python src/scripts/ingestions/__obligaciones__.py`
5. `python src/scripts/ingestions/__cuentas__.py`
