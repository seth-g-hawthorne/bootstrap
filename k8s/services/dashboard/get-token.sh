#!/bin/bash
secret=$(kubectl -n kubernetes-dashboard get secret | grep admin-user | awk '{print $1}')
kubectl -n kubernetes-dashboard describe secret ${secret} | grep "token:"
echo Browse to: http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/