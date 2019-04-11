# ansible-taiga
  Install taiga all components.
  官方文档http://taigaio.github.io/taiga-doc/dist/setup-production.html

# Use
  -e deploy_hosts 指定部署主机名，具体配置在hosts_all文件中，数据库用户名、密码及其它在group_vars/中修改配置

  ansible-playbook -i hosts_all
  play_taiga-all.yml -e deploy_hosts=server2

  初始化样例数据在 playbook_taiga\roles\taiga_back\scripts\initial_database.sh  设置为只有服务名为server3才加载用户样例 python manage.py sample_data。
