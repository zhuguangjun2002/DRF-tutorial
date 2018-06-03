#!/bin/sh

USERNAME="girls"
#为`应用`创建一个`用户`-`girls`，
#附给`系统组`-`webapps`。
sudo groupadd --system webapps
sudo useradd --system --gid webapps --home /webapps/djangogirls $USERNAME

#为用户`girls`设定密码
passwd $USERNAME
#默认密码 为:yantai2018

# 创建`djangogirls`目录
#创建一个目录，以便存储你的应用程序，在目录`/webapps/djangogrils/` ,并且，修改该目录的`所有者`为你的用户`girls`.
#sudo mkdir -p /webapps/djangogirls/
#sudo chown girls /webapps/djangogirls

# 创建一个python3的虚拟环境
#cd djangogirls
#virtualenv -p python3 env

# 导入脚本
#source env/bin/activate

# git clone代码
#git clone https://github.com/zhuguangjun2002/my-first-blog.git

# 安装依赖包
#cd my-first-blog
#pip install -r requirements.txt

