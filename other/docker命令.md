centos7安装docker
```bash
yum -y install docker-io 
```
启动docker
```bash
systemctl restart docker
```


docker安装mysql (dockehub上面拉取)
```bash
docker pull mysql
```
启动mysql容器
```bash
docker run -e MYSQL__ROOT_PASSWORD=123456 -p 33306:3306 -d docker.io/mysql
```
**参数说明 **-e：设置环境变量；如设置数据库密码的三个参数为: MYSQL_ROOT_PASSWORD、MYSQL_ALLOW_EMPTY_PASSWORD 、MYSQL_RANDOM_ROOT_PASSWORD -p：映射端口；如将宿主机的3306端口映射到容器中的3306端口上。 -d：后台运行
将宿主机的33306端口映射到容器的3306端口，外网访问宿主机的33306，就是在访问容器的3306端口

进入容器命令
```bash
docker exec -it 容器id /bin/bash
```
安全退出容器，容器不会挂掉
```bash
ctrl + p + q
```
docker基本命令
```bash
- docker images 查看镜像
- docker ps 查询运行中的容器
- docker ps -a 查询所有的容器，包括死亡的容器
- docker rm 移除容器或镜像
```

blognginx.config
```bash
server{
	listen 80;
	server_name 47.102.100.231;
	
	root /home/code/dist;
	index index.html;
	location /api/ {
		proxy_pass http://47.102.100.231:8000;
	}
}
```