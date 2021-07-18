# Initium: KinD
Scripts and resources for running and working with kind (docker-based Kubernetes) clusters

## Usage
   1. `bin/kind-install` - Install kind on ubuntu
   1. `bin/kind-cluster` [create | delete | status ] - Operate on kind clusters. Run with no arguments for more help
   1. `kubectl-init.so` - Source this file to generate a kubectl configuration and set `KUBECONFIG` to point to it
   
## Related Information
   * [kind](https://kind.sigs.k8s.io/)
   * [kind GitHub](https://github.com/kubernetes-sigs/kind)