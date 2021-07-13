# Initium: Kind
Scripts and resources for running and working with kind (docker-based Kubernetes) clusters

## Scripts
   * `install-kind.sh` - Install kind on ubuntu
   * `cluster.sh` [create | delete | status ] - Operate on kind clusters. Run with no arguments for more help
   * `kubectl-init.so` - Source this file to generate a kubectl configuration and set `KUBECONFIG` to point to it
   
## Related Information
   * [kind](https://kind.sigs.k8s.io/)
   * [kind GitHub](https://github.com/kubernetes-sigs/kind)