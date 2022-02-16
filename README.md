# Kubernetes local cluster setup

## Pre-requisites

1. Install docker
   
## Create a 3-node cluster
```$ minikube start --nodes 3 -p multinode-k8s-cluster```


## Verify cluster
```
$ kubectl get no -o wide
NAME                        STATUS   ROLES                  AGE   VERSION   INTERNAL-IP    EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION      CONTAINER-RUNTIME
multinode-k8s-cluster       Ready    control-plane,master   60s   v1.23.1   192.168.67.2   <none>        Ubuntu 20.04.2 LTS   5.13.0-28-generic   docker://20.10.12
multinode-k8s-cluster-m02   Ready    <none>                 39s   v1.23.1   192.168.67.3   <none>        Ubuntu 20.04.2 LTS   5.13.0-28-generic   docker://20.10.12
multinode-k8s-cluster-m03   Ready    <none>                 24s   v1.23.1   192.168.67.4   <none>        Ubuntu 20.04.2 LTS   5.13.0-28-generic   docker://20.10.12
```

## Deploy app
```$ kubectl apply -f deployment.yaml```


## Check service URL

```
$ minikube service list -p multinode-k8s-cluster
|-------------|------------|--------------|---------------------------|
|  NAMESPACE  |    NAME    | TARGET PORT  |            URL            |
|-------------|------------|--------------|---------------------------|
| default     | hello      |           80 | http://192.168.67.2:31000 |
| default     | kubernetes | No node port |                           |
| kube-system | kube-dns   | No node port |                           |
|-------------|------------|--------------|---------------------------|
```


## Test service

```curl http://192.168.67.2:31000```


## Install Helm

## Install Prometheus and Grafana from Bitnami charts

### Install dashboards
 - https://grafana.com/grafana/dashboards/7249
 - https://grafana.com/grafana/dashboards/11142
    

## Install Chaos Mesh
``` curl -sSL https://mirrors.chaos-mesh.org/v2.1.3/install.sh | bash ```

### Create chaos experiment
``` kubectl apply -f network-delay-experiment.yaml ```

## Install Prometheus and Grafana Helm charts
1. helm repo add bitnami https://charts.bitnami.com/bitnami
2. helm install bitnami-grafana bitnami/grafana
3. helm install bitnami-prometheus bitnami/kube-prometheus

### Get Grafana credentials
```
$ echo "Username: admin"
$ echo "Password: $(kubectl get secret bitnami-grafana-admin --namespace default -o jsonpath="{.data.GF_SECURITY_ADMIN_PASSWORD}" | base64 --decode)"
```


### Start Prometheus UI

```
$ echo "Prometheus URL: http://127.0.0.1:9090/"

$ kubectl port-forward --namespace default svc bitnami-prometheus-kube-pr-prometheus 9090:9090
```
