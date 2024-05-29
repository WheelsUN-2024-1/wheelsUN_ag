docker rmi jivegabe/image-wheelsun_ag-ldap_cloud
docker login
docker tag image-wheelsun_ag:latest jivegabe/image-wheelsun_ag-ldap_cloud
docker push jivegabe/image-wheelsun_ag-ldap_cloud
docker rmi jivegabe/image-wheelsun_ag-ldap_cloud
docker rmi image-wheelsun_ag
Read-Host -Prompt "Press Enter to exit"