# Installing gdal in virtual environment.
You need to download gdal from this link: https://www.lfd.uci.edu/~gohlke/pythonlibs/#gdal.
After downloading it, put it in your working directory of your django project.
Then run the command
``` 
  pip install GDAL-3.4.3-cp310-cp310-win_amd64.whl
``` 

Note: You need to install right gdal according to your python version on your pc.
For example for above file, 
   310 is python version 3.10 

Also Check the setting.py(change the name of virtual environment if neccessary).  
``` 
if DEBUG == True:
    os.environ['PATH'] = os.path.join(BASE_DIR, 'ZFLVirtual\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(BASE_DIR, 'ZFLVirtual\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']
    GDAL_LIBRARY_PATH = os.path.join(BASE_DIR, 'ZFLVirtual\Lib\site-packages\osgeo\gdal304.dll')
``` 


# POSTGIS SETUP
You need to install Application Stack Manager  to install Postgis.
Video Source: https://www.youtube.com/watch?v=tTUM9XfDvqk

Then, type the following command.
i. psql;
ii. CREATE DATABASE CMS;
iii. CREATE USER Sam WITH PASSWORD 'sammer123';
iv. grant all privileges on database CMS to Sam;
v. CREATE EXTENSION postgis;
   This last query does the thing.

PostGIS is a spatial database extender for PostgreSQL object-relational database. It adds support for geographic objects allowing location queries to be run in SQL



# Understanding Two Types oF model
  Customer -> Only pays for food.
  Vendor -> Have a Restaurant and manages items, categories and also can buy food.