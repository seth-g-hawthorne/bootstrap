# Initium: Kubernetes Google Cloud
Scripts for creating and interacting with Google Cloud hosted Kubernetes clusters

## Getting Started

### Prerequisits 
  1. Browse to: [Google Cloud Console](https://console.cloud.google.com/)
    * Goto Kubernetes Engine and click "Enable"
  1. `bin/gke-install.sh`
  1. Cusomize values in `config.so` or specify values via command flags
  1. `gcloud init`
     * Respond to prompts

### Create a cluster
  1. `bin/gke-cluster-create` <name> - Create a 2 node cluster
  1. `kubectl get nodes` - List nodes
  1. `bin/gke-cluster-admin-role` - Enable admin access

### Delete a cluster
  1. `bin/gke-cluster-delete`


## Useful Information
   * [Google Cloud SDK Docs](https://cloud.google.com/sdk/docs)
   * [Kubernetes on GKE](https://zero-to-jupyterhub.readthedocs.io/en/latest/kubernetes/google/step-zero-gcp.html#)