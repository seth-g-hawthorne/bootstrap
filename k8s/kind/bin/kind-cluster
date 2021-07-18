#!/bin/bash
#	
# Adapted from:	
# https://github.com/kubernetes-sigs/kind/commits/master/site/static/examples/kind-with-registry.sh	
#	
# Modifications:
#  - Command line argument support
#  - Support for creating multiple nodes
#  - Configure insecure registry 

set -o errexit

function usage {
    echo "$0 create [--name <name>] [--workers <count>] [--version <k8s-version>]"
    echo "             delete [--name <name>] [--all]"
    echo "             kubeconfig"    
    echo "             status"    
    exit 1
}

REQUIRED_KIND_VERSION="v0.11*"
kind_version=$(kind version | cut -d ' ' -f 2)
if [ $kind_version == $REQUIRED_KIND_VERSION ]; then
    echo "**** Error: Must run with kind version ${REQUIRED_KIND_VERSION}"
    exit 3
fi 

# K8s image versions for this version of Kind (see https://github.com/kubernetes-sigs/kind/releases)
declare -A K8S_VERSIONS 
K8S_VERSIONS['1.21']=kindest/node:v1.21.1@sha256:69860bda5563ac81e3c0057d654b5253219618a22ec3a346306239bba8cfa1a6
K8S_VERSIONS['1.20']=kindest/node:v1.20.7@sha256:cbeaf907fc78ac97ce7b625e4bf0de16e3ea725daf6b04f930bd14c67c671ff9
K8S_VERSIONS['1.19']=kindest/node:v1.19.11@sha256:07db187ae84b4b7de440a73886f008cf903fcf5764ba8106a9fd5243d6f32729
K8S_VERSIONS['1.18']=kindest/node:v1.18.19@sha256:7af1492e19b3192a79f606e43c35fb741e520d195f96399284515f077b3b622c
K8S_VERSIONS['1.17']=kindest/node:v1.17.17@sha256:66f1d0d91a88b8a001811e2f1054af60eef3b669a9a74f9b6db871f2f1eeed00
K8S_VERSIONS['1.16']=kindest/node:v1.16.15@sha256:83067ed51bf2a3395b24687094e283a7c7c865ccc12a8b1d7aa673ba0c5e8861
K8S_VERSIONS['1.15']=kindest/node:v1.15.12@sha256:b920920e1eda689d9936dfcf7332701e80be12566999152626b2c9d730397a95
K8S_VERSIONS['1.14']=kindest/node:v1.14.10@sha256:f8a66ef82822ab4f7569e91a5bccaf27bceee135c1457c512e54de8c6f7219f8
k8s_version='1.21'
k8s_image=${K8S_VERSIONS[$k8s_version]}
echo $k8s_image

function version_error() {
  echo "**** ERROR: Unexpected Kubernetes version" 
  echo "            expected: ${!K8s_VERSIONS[@]}"
  exit 2
}

function reg_kill {
    echo "o Stopping: ${reg_name}"
    docker kill ${reg_name}
    docker rm ${reg_name}
}

cluster_name="${KIND_CLUSTER_NAME:-kind}"
delete_all=false
reg_enabled=true
reg_name='kind-registry'
reg_port='5000'
reg_ip_selector='{{.NetworkSettings.Networks.kind.IPAddress}}'
reg_network='kind'
worker_count=0
ingress_http_port="${KIND_INGRESS_HTTP_PORT:-81}"
ingress_https_port="${KIND_INGRESS_HTTPS_PORT:-444}"

# Parse them arguments 
[[ $# -eq 0 ]] && usage
command="$1"
shift
while [[ $# -gt 0 ]]
do
  case "$1" in
    --all)
    [[ $command != 'delete' ]] && usage
    delete_all=true
    ;;

    -n|--name)
    [[ $# -lt 2 ]] && usage
    cluster_name="$2"
    shift
    ;;

    --workers | -w)
    [[ $# -lt 2 || $command != "create" ]] && usage
    worker_count="$2"
    shift
    ;;

    --no-registry | --no-reg)
    [[ $command != "create" ]] && usage
    reg_enabled=0
    ;;

    --version | -v)
    [[ $command != "create" ]] && usage
    shift
    k8s_image=${K8S_VERSIONS[$1]}
    [[ $ks_image != "" ]] && version_error
    ;;

    *)
    usage
    ;;
  esac
shift
done

# Execute command
case "${command}" in
  create)
  # Drop through for create logic 
  ;;

  delete)
  echo "--> Deleting cluster: ${cluster_name}"
  kind delete cluster --name "${cluster_name}"
  if [[ $delete_all = true ]]; then
    reg_kill
    docker network rm "${cluster_name}"
  fi
  exit 0
  ;;

  kubeconfig)
  kind get kubeconfig
  exit 0
  ;;

  status)
  echo "Status of cluster ${cluster_name}"
  docker ps | grep -q "${cluster_name}"
  if [[ $? == 0 ]]; then
    docker ps -a --no-trunc --filter name=^/kind- --format "table {{.Names}}\t{{.Status}}\t{{.Ports}}"
  else
    echo "Not running"
  fi
  exit 0
  ;;

  *)
  if [[ ${command} -gt 0 ]] ; then
    echo "Unrecognized command: $command"
  fi
  usage
  ;;
esac 

# If the registry exists but is using different network, recreate it
reg_running="$(docker inspect -f '{{.State.Running}}' "${reg_name}" 2>/dev/null || true)"
if [[ $reg_running == 'true' ]]; then
  reg_ip="$(docker inspect -f ${reg_ip_selector} "${reg_name}")"
  if [ "${reg_ip}" = '' ]; then
    reg_kill
    reg_running="false"
  fi
fi

if [[ $reg_running != 'true' ]]; then
  echo "--> Creating network: ${reg_network}"
  docker network create "${reg_network}" || true
  
  echo "--> Creating registry: ${reg_name}"
  docker run \
    -d --restart=always -p "${reg_port}:5000" --name "${reg_name}" --net "${reg_network}" registry:2
else
  echo "--> Registry is running"
fi

reg_ip="$(docker inspect -f ${reg_ip_selector} "${reg_name}")"
if [ "${reg_ip}" = "" ]; then
  echo "Error creating registry: no IPAddress found at: ${reg_ip_selector}"
  exit 1
fi
echo "    - registry IP: ${reg_ip}"

# Request specified number of worker nodes
nodes=""
if [[ $worker_count -gt 0 ]]; then 
  nodes="- role: worker"
  for (( i=1; i<$worker_count; i++ ))
  do
      nodes=${nodes}"\n- role: worker"
  done
fi 

# create a cluster with the local registry enabled in containerd
echo "--> Creating cluster: ${cluster_name}"
cat <<EOF | kind create cluster --name "${cluster_name}" --config=-
kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  kubeadmConfigPatches:
  - |
    kind: InitConfiguration
    nodeRegistration:
      kubeletExtraArgs:
        node-labels: "ingress-ready=true"
  extraPortMappings:
  - containerPort: 80
    hostPort: ${ingress_http_port}
    protocol: TCP
  - containerPort: 443
    hostPort: ${ingress_https_port}
    protocol: TCP
`echo -e ${nodes}`
# Disabled RemoveSelfLink option to address nfs-client provisioner issue in kubernetes v1.20
featureGates:
  "RemoveSelfLink": false
containerdConfigPatches: 
- |-
  [plugins."io.containerd.grpc.v1.cri".registry.mirrors."localhost:${reg_port}"]
    endpoint = ["http://${reg_ip}:${reg_port}"]
  [plugins."io.containerd.grpc.v1.cri".registry.configs]
    [plugins."io.containerd.grpc.v1.cri".registry.configs."localhost:5000"]
      insecure_skip_verify = true
EOF

echo
echo "Source 'kubectl-init.so' to configure kubectl"
echo
