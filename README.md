# Setup
1) cd /var/www
2) sudo mkdir project_name
3) sudo chown user:user project_name
4) git clone https://github.com/wayne-abarquez/solar-demo.git project_name
5) cd project_name/
6) bin/setup.sh
7) bin/createdb.sh
8) bin/setup-nginx.sh
9) python manage.py db upgrade
10) bin/local/run-app.sh

# For Development
Note: it is using port 82
1) bin/local/setup-client-tools.sh
2) bin/local/setup-nginx.sh
3) cd client
4) npm install
5) bower install
6) then you can execute gulp tasks.
   * gulp build and gulp watch
7) bin/local/run-app.sh

# Set it to your Git Repo
git remote add origin https://github.com/user/repo.git

