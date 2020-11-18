# PythonOne
Installing Python3 on Ubuntu 20.04

hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin$ sudo apt update
[sudo] password for hduser: 
Hit:1 http://in.archive.ubuntu.com/ubuntu focal InRelease
Hit:2 http://in.archive.ubuntu.com/ubuntu focal-updates InRelease                                                                            
Hit:3 https://download.docker.com/linux/ubuntu focal InRelease                                                                               
Hit:4 http://in.archive.ubuntu.com/ubuntu focal-backports InRelease                                                              
Hit:5 http://ppa.launchpad.net/dawidd0811/neofetch/ubuntu focal InRelease                 
Hit:6 http://security.ubuntu.com/ubuntu focal-security InRelease    
Hit:7 https://deb.tableplus.com/debian tableplus InRelease
Reading package lists... Done
Building dependency tree       
Reading state information... Done
All packages are up to date.
hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin$ sudo apt -y upgrade
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Calculating upgrade... Done
The following packages were automatically installed and are no longer required:
  linux-headers-5.4.0-52 linux-headers-5.4.0-52-generic linux-image-5.4.0-52-generic linux-modules-5.4.0-52-generic
  linux-modules-extra-5.4.0-52-generic
Use 'sudo apt autoremove' to remove them.
0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
hduser@thanoojubuntu-Inspiron-3521:~$ python3 -V
Python 3.8.5
hduser@thanoojubuntu-Inspiron-3521:~$ sudo apt install -y python3-pip
[sudo] password for hduser: 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-5.4.0-52 linux-headers-5.4.0-52-generic
  linux-image-5.4.0-52-generic linux-modules-5.4.0-52-generic
  linux-modules-extra-5.4.0-52-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  libpython3-dev libpython3.8-dev python-pip-whl python3-dev
  python3-setuptools python3-wheel python3.8-dev
Suggested packages:
  python-setuptools-doc
The following NEW packages will be installed:
  libpython3-dev libpython3.8-dev python-pip-whl python3-dev python3-pip
  python3-setuptools python3-wheel python3.8-dev
0 upgraded, 8 newly installed, 0 to remove and 0 not upgraded.
Need to get 6,847 kB of archives.
After this operation, 25.5 MB of additional disk space will be used.
Get:1 http://in.archive.ubuntu.com/ubuntu focal-updates/main amd64 libpython3.8-dev amd64 3.8.5-1~20.04 [3,941 kB]
Get:2 http://in.archive.ubuntu.com/ubuntu focal/main amd64 libpython3-dev amd64 3.8.2-0ubuntu2 [7,236 B]
Get:3 http://in.archive.ubuntu.com/ubuntu focal-updates/universe amd64 python-pip-whl all 20.0.2-5ubuntu1.1 [1,799 kB]
Get:4 http://in.archive.ubuntu.com/ubuntu focal-updates/main amd64 python3.8-dev amd64 3.8.5-1~20.04 [514 kB]
Get:5 http://in.archive.ubuntu.com/ubuntu focal/main amd64 python3-dev amd64 3.8.2-0ubuntu2 [1,212 B]
Get:6 http://in.archive.ubuntu.com/ubuntu focal/main amd64 python3-setuptools all 45.2.0-1 [330 kB]
Get:7 http://in.archive.ubuntu.com/ubuntu focal/universe amd64 python3-wheel all 0.34.2-1 [23.8 kB]
Get:8 http://in.archive.ubuntu.com/ubuntu focal-updates/universe amd64 python3-pip all 20.0.2-5ubuntu1.1 [230 kB]
Fetched 6,847 kB in 13s (520 kB/s)                                             
Selecting previously unselected package libpython3.8-dev:amd64.
(Reading database ... 243240 files and directories currently installed.)
Preparing to unpack .../0-libpython3.8-dev_3.8.5-1~20.04_amd64.deb ...
Unpacking libpython3.8-dev:amd64 (3.8.5-1~20.04) ...
Selecting previously unselected package libpython3-dev:amd64.
Preparing to unpack .../1-libpython3-dev_3.8.2-0ubuntu2_amd64.deb ...
Unpacking libpython3-dev:amd64 (3.8.2-0ubuntu2) ...
Selecting previously unselected package python-pip-whl.
Preparing to unpack .../2-python-pip-whl_20.0.2-5ubuntu1.1_all.deb ...
Unpacking python-pip-whl (20.0.2-5ubuntu1.1) ...
Selecting previously unselected package python3.8-dev.
Preparing to unpack .../3-python3.8-dev_3.8.5-1~20.04_amd64.deb ...
Unpacking python3.8-dev (3.8.5-1~20.04) ...
Selecting previously unselected package python3-dev.
Preparing to unpack .../4-python3-dev_3.8.2-0ubuntu2_amd64.deb ...
Unpacking python3-dev (3.8.2-0ubuntu2) ...
Selecting previously unselected package python3-setuptools.
Preparing to unpack .../5-python3-setuptools_45.2.0-1_all.deb ...
Unpacking python3-setuptools (45.2.0-1) ...
Selecting previously unselected package python3-wheel.
Preparing to unpack .../6-python3-wheel_0.34.2-1_all.deb ...
Unpacking python3-wheel (0.34.2-1) ...
Selecting previously unselected package python3-pip.
Preparing to unpack .../7-python3-pip_20.0.2-5ubuntu1.1_all.deb ...
Unpacking python3-pip (20.0.2-5ubuntu1.1) ...
Setting up python3-setuptools (45.2.0-1) ...
Setting up python3-wheel (0.34.2-1) ...
Setting up libpython3.8-dev:amd64 (3.8.5-1~20.04) ...
Setting up python3.8-dev (3.8.5-1~20.04) ...
Setting up python-pip-whl (20.0.2-5ubuntu1.1) ...
Setting up libpython3-dev:amd64 (3.8.2-0ubuntu2) ...
Setting up python3-dev (3.8.2-0ubuntu2) ...
Setting up python3-pip (20.0.2-5ubuntu1.1) ...
Processing triggers for man-db (2.9.1-1) ...
hduser@thanoojubuntu-Inspiron-3521:~$ pip3 install numpy
Collecting numpy
  Downloading numpy-1.19.4-cp38-cp38-manylinux2010_x86_64.whl (14.5 MB)
     |████████████████████████████████| 14.5 MB 329 kB/s 
Installing collected packages: numpy
  WARNING: The scripts f2py, f2py3 and f2py3.8 are installed in '/home/hduser/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed numpy-1.19.4
hduser@thanoojubuntu-Inspiron-3521:~$ gedit ~/.bashrc
hduser@thanoojubuntu-Inspiron-3521:~$ source ~/.bashrc
hduser@thanoojubuntu-Inspiron-3521:~$ source ~/.bashrc
duser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin$ echo $PATH
/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/local/hadoop/bin:/usr/lib/jvm/java-1.8.0-openjdk-amd64/bin:/usr/local/hadoop/sbin:/home/hduser/softwares/apache-hive-3.1.2-bin/bin:/usr/local/spark-2.4.6-bin-hadoop2.7/bin:/usr/local/spark-2.4.6-bin-hadoop2.7/sbin:/usr/local/spark-2.4.6-bin-hadoop2.7/bin:/usr/local/spark-2.4.6-bin-hadoop2.7/sbin:/usr/local/hadoop/bin:/usr/lib/jvm/java-1.8.0-openjdk-amd64/bin:/usr/local/hadoop/sbin:/home/hduser/softwares/apache-hive-3.1.2-bin/bin:/usr/local/spark-2.4.6-bin-hadoop2.7/bin:/usr/local/spark-2.4.6-bin-hadoop2.7/sbin:/usr/local/kafka_2.13-2.6.0/bin:/usr/local/kafka_2.13-2.6.0/config:/home/hduser/.local/bin
hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin
hduser@thanoojubuntu-Inspiron-3521:~$ pip3 install numpy
Requirement already satisfied: numpy in ./.local/lib/python3.8/site-packages (1.19.4)
hduser@thanoojubuntu-Inspiron-3521:~$ sudo apt install -y python3-venv
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages were automatically installed and are no longer required:
  linux-headers-5.4.0-52 linux-headers-5.4.0-52-generic linux-image-5.4.0-52-generic linux-modules-5.4.0-52-generic
  linux-modules-extra-5.4.0-52-generic
Use 'sudo apt autoremove' to remove them.
The following additional packages will be installed:
  python3.8-venv
The following NEW packages will be installed:
  python3-venv python3.8-venv
0 upgraded, 2 newly installed, 0 to remove and 0 not upgraded.
Need to get 6,668 B of archives.
After this operation, 38.9 kB of additional disk space will be used.
Get:1 http://in.archive.ubuntu.com/ubuntu focal-updates/universe amd64 python3.8-venv amd64 3.8.5-1~20.04 [5,440 B]
Get:2 http://in.archive.ubuntu.com/ubuntu focal/universe amd64 python3-venv amd64 3.8.2-0ubuntu2 [1,228 B]
Fetched 6,668 B in 1s (8,707 B/s)        
Selecting previously unselected package python3.8-venv.
(Reading database ... 243779 files and directories currently installed.)
Preparing to unpack .../python3.8-venv_3.8.5-1~20.04_amd64.deb ...
Unpacking python3.8-venv (3.8.5-1~20.04) ...
Selecting previously unselected package python3-venv.
Preparing to unpack .../python3-venv_3.8.2-0ubuntu2_amd64.deb ...
Unpacking python3-venv (3.8.2-0ubuntu2) ...
Setting up python3.8-venv (3.8.5-1~20.04) ...
Setting up python3-venv (3.8.2-0ubuntu2) ...
Processing triggers for man-db (2.9.1-1) ...
hduser@thanoojubuntu-Inspiron-3521:~$ pwd
/home/hduser
hduser@thanoojubuntu-Inspiron-3521:~$ mkdir environments
hduser@thanoojubuntu-Inspiron-3521:~$ cd environments/
hduser@thanoojubuntu-Inspiron-3521:~/environments$ ls -ltr
total 0
hduser@thanoojubuntu-Inspiron-3521:~/environments$ cd ..
hduser@thanoojubuntu-Inspiron-3521:~$ ls -ltr
total 4996
...
drwxrwxr-x 2 hduser hduser    4096 Nov 18 22:34 environments
hduser@thanoojubuntu-Inspiron-3521:~$ cd environments/
hduser@thanoojubuntu-Inspiron-3521:~/environments$ python3 -m venv my_env
hduser@thanoojubuntu-Inspiron-3521:~/environments$ ls -ltr
total 4
drwxrwxr-x 6 hduser hduser 4096 Nov 18 22:35 my_env
hduser@thanoojubuntu-Inspiron-3521:~/environments$ cd my_env/
hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env$ ls -ltr
total 20
-rw-rw-r-- 1 hduser hduser   69 Nov 18 22:35 pyvenv.cfg
lrwxrwxrwx 1 hduser hduser    3 Nov 18 22:35 lib64 -> lib
drwxrwxr-x 3 hduser hduser 4096 Nov 18 22:35 lib
drwxrwxr-x 2 hduser hduser 4096 Nov 18 22:35 include
drwxrwxr-x 3 hduser hduser 4096 Nov 18 22:35 share
drwxrwxr-x 2 hduser hduser 4096 Nov 18 22:35 bin
hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env$ cd bin/
hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin$ ls -ltr
total 44
lrwxrwxrwx 1 hduser hduser   16 Nov 18 22:35 python3 -> /usr/bin/python3
lrwxrwxrwx 1 hduser hduser    7 Nov 18 22:35 python -> python3
-rwxrwxr-x 1 hduser hduser  258 Nov 18 22:35 easy_install-3.8
-rwxrwxr-x 1 hduser hduser  258 Nov 18 22:35 easy_install
-rwxrwxr-x 1 hduser hduser  249 Nov 18 22:35 pip3.8
-rwxrwxr-x 1 hduser hduser  249 Nov 18 22:35 pip3
-rwxrwxr-x 1 hduser hduser  249 Nov 18 22:35 pip
-rw-r--r-- 1 hduser hduser 8834 Nov 18 22:35 Activate.ps1
-rw-r--r-- 1 hduser hduser 2420 Nov 18 22:35 activate.fish
-rw-r--r-- 1 hduser hduser 1268 Nov 18 22:35 activate.csh
-rw-r--r-- 1 hduser hduser 2216 Nov 18 22:35 activate
hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin$ source activate
(my_env) hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin$ nano hello.py
(my_env) hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin$ nano hello.py
(my_env) hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin$ python3 hello.py 
Hello, World!
(my_env) hduser@thanoojubuntu-Inspiron-3521:~/environments/my_env/bin$
