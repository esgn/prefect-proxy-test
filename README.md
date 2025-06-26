**Update** : https://github.com/PrefectHQ/prefect/pull/18374 has fixed the issue. This repository may be used for more testing of Prefect using corporate proxy.

# prefect-proxy-test

Playground to test Prefect + Squid for possible incompatibilities.  

Based on https://github.com/PrefectHQ/prefect/tree/main/scripts/proxy-test (and also on https://github.com/rpeden/prefect-docker-compose).

## Test with Squid proxy

### Deploy Prefect + Squid

```
docker compose up -d
```

### Create venv

```
python3 -m venv prefect_venv
source prefect_venv/bin/activate
pip install -U pip setuptools wheel
pip install -U prefect
```

### Export environment variables in current session

```
source set_env_vars.sh
```

Verify proxy settings and PREFECT_API_URL are correctly set

```
env | grep -i proxy
env | grep PREFECT_API_URL
```

### Try run and deployment of a simple Hello World flow

This should work with problem

```
python test_flow.py
```

This should show an asyncio error  `Task pending got Future attached to a different loop`

```
python test_deployment.py
```

### Shut down everything

Remove containers, networks and volumes

```
docker compose down -v
```
