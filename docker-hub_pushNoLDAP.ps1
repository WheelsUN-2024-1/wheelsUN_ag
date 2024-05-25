docker rmi jivegabe/image-wheelsun_ag-no_ldap
docker login
docker tag image-wheelsun_ag:latest jivegabe/image-wheelsun_ag-no_ldap
docker push jivegabe/image-wheelsun_ag-no_ldap
docker rmi jivegabe/image-wheelsun_ag-no_ldap
docker rmi image-wheelsun_ag
Read-Host -Prompt "Press Enter to exit"