# # Launchpad: k8s/ubuntu

Scripts useful for manually creating Kubernetes clusters on Ubuntu (16.04, 18.04)

## Create a Kubernetes Cluster

  1. For the Master node, create an Ubuntu instance and run `init-master.sh`, which performs the following:   
      * `init-ubuntu-node.sh`
        * Install docker (`install-docker.sh`)
        * Configure Kubernetes required Ubuntu settings (`config-ubuntu.sh`)    
        * Install K8s components (`install-k8s.sh`)  
      * Runs `kubeadm init` and creates a `join-cluster.sh` script which must be run to have worker nodes join the cluster. 
      * Configure kubectl (`init-kubctl.sh`)      
      * Install Flannel as the CNI (`install-cni.sh`)      
      * Install [kubectx](https://github.com/ahmetb/kubectx) and [kubens](https://github.com/ahmetb/kubectx) (`kuinstall-kubectx.sh`) 
    
  1. For each Worker Node, create an Ubuntu instance and run `init-worker.sh`, which performs the following:   
     * `init-ubuntu-node.sh` (see above)
     * copy `join-cluster.sh` from the master node and run it 


## Useful Information
### Tools 
  * [50 USeful Kubernetes Tools](https://caylent.com/50-useful-kubernetes-tools-for-2020)