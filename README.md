# Trashbox

domainname

    |
    |
  
lb1,lb2...(haproxy)
  
    |
    |
  
gateway1,gateway2...(Django,Flask)
  
    |
    |
  
controller--swift-objnode1,swiftobjnode2...
              |
              
              |
              
            storage(san, localdisk...)

# TODO:

1. Investigate swift deployment
  - puppet(recommend): https://github.com/hastexo/kickstack 
  - devstack

2. Test performance of IO forward(Python, Java, nodejs)
  - https://wiki.openstack.org/wiki/SDKs

3. Framework
  - Django
  - Flask
