The `valory/p2p_libp2p:0.26.0` connection allows AEAs to create a peer-to-peer communication network. In particular, the connection creates an overlay network which maps agents' public keys to IP addresses.

## Local demo

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>Currently <code>p2p_libp2p</code> does not support the 
  ethereum keys generated by open-aea-ledger-ethereum yet.
  This does not affect the agents' ability to interact with the 
  ethereum ledger and solely necessitates a separate set of 
  cosmos keys for establishing the libp2p connection.
</p>
</div>

First, make sure you have installed the crypto plugin
of the target test-net. 
``` bash
pip install open-aea-ledger-cosmos
pip install open-aea-ledger-ethereum
```

### Create and run the genesis AEA

Create one AEA as follows:

``` bash
aea create my_genesis_aea
cd my_genesis_aea
aea add connection valory/p2p_libp2p:0.1.0
aea config set agent.default_connection valory/p2p_libp2p:0.1.0
aea install
aea build
```

Establish the <a href="../por">proof of representation</a>:

``` bash
aea generate-key ethereum
aea add-key ethereum ethereum_private_key.txt
aea generate-key cosmos cosmos_connection_private_key.txt
aea add-key cosmos cosmos_connection_private_key.txt --connection
aea issue-certificates
```

Run the AEA:

``` bash
aea run --connections valory/p2p_libp2p:0.1.0
```

Once you see a message of the form `To join its network use multiaddr 'SOME_ADDRESS'` take note of the address. (Alternatively, use `aea get-multiaddress open-aea -c -i valory/p2p_libp2p:0.1.0 -u public_uri` to retrieve the address.)
This is the entry peer address for the local <a href="../acn">agent communication network</a> created by the genesis AEA.

### Create and run another AEA

Create a second AEA:

``` bash
aea create my_other_aea
cd my_other_aea
aea add connection valory/p2p_libp2p:0.1.0
aea config set agent.default_connection valory/p2p_libp2p:0.1.0
aea install
aea build
```

Establish the <a href="../por">proof of representation</a>:

``` bash
aea generate-key ethereum
aea add-key ethereum ethereum_private_key.txt
aea generate-key cosmos cosmos_connection_private_key.txt
aea add-key cosmos cosmos_connection_private_key.txt --connection
aea issue-certificates
```

Provide the AEA with the information it needs to find the genesis:

``` bash
aea config set --type dict vendor.valory.connections.p2p_libp2p.config \
'{
  "delegate_uri": "127.0.0.1:11001",
  "entry_peers": [<AEA_P2P_ENTRY_URI_1>, <AEA_P2P_ENTRY_URI_2>],
  "local_uri": "127.0.0.1:9001",
  "log_file": "libp2p_node.log",
  "public_uri": "127.0.0.1:9001"
}'
```
Here `[<AEA_P2P_ENTRY_URI_1>, <AEA_P2P_ENTRY_URI_2>]` represents a list of multi addresses displayed in the log output of the genesis AEA.

Run the AEA:

``` bash
aea run --connections valory/p2p_libp2p:0.1.0
```

You can inspect the `libp2p_node.log` log files of the AEA to see how they discover each other.

<div class="admonition note">
  <p class="admonition-title">Note</p>
  <p>Currently <code>p2p_libp2p</code> connection limits the total message size to 3 MB.
</p>
</div>

## Deployed agent communication network

You can connect to the deployed public test network by adding one or multiple of the following addresses as the `p2p_libp2p` connection's `entry_peers`:

``` yaml
/dns4/staging.acn.autonolas.tech/tcp/9003/p2p/16Uiu2HAkzqwxz5HdbnXS6mB4nTwJ3WysQa6udvbZ3te2sCHZ6ih2
```
``` yaml
/dns4/staging.acn.autonolas.tech/tcp/9004/p2p/16Uiu2HAmCQqXLFWaqqUv8hFdFPDwwNQf9qEQox8Kcf78heb33e7x
```

Specifically, in an AEAs configuration `aea-config.yaml` add the above addresses for `entry_peers` as follows:
``` yaml
---
public_id: valory/p2p_libp2p:0.1.0
type: connection
config:
  delegate_uri: null
  entry_peers: [/dns4/staging.acn.autonolas.tech/tcp/9003/p2p/16Uiu2HAkzqwxz5HdbnXS6mB4nTwJ3WysQa6udvbZ3te2sCHZ6ih2,/dns4/staging.acn.autonolas.tech/tcp/9004/p2p/16Uiu2HAmCQqXLFWaqqUv8hFdFPDwwNQf9qEQox8Kcf78heb33e7x]
  public_uri: null
  local_uri: 127.0.0.1:9001
```

Note, this configuration change must be made for all agents attempting to communicate with each other via the Agent Communication Network. For example, in demos involving two agents, both agents will need the above modifications to their respective `aea-config.yaml` file. However, remember to use different ports in `local_uri.` This will allow both agents to default to this communication network without the added overhead of opening ports and specifying hosts on the individual host machines running each agent.


## Configuring the `connection.yaml` entries:

To learn more about how to configure your `valory/p2p_libp2p:0.1.0` connection consult the `README.md` file supplied with the connection package.

## Running Go peer standalone

You can run a peer node in _standalone mode_; that is, as a Go process with no dependency on the AEA framework. To facilitate such a deployment, we provide a script
 <a href="https://github.com/valory-xyz/open-aea/blob/main/scripts/acn/run_acn_node_standalone.py" target="_blank">`run_acn_node_standalone.py`</a>
 and a corresponding 
 <a href="https://github.com/valory-xyz/open-aea/blob/main/scripts/acn/Dockerfile" target="_blank">Dockerfile</a>.

First, you need to build the node's binary (`libp2p_node`) either:

- locally
  ``` bash
  git clone https://github.com/valory-xyz/open-acn/
  cd open-acn
  go build
  chmod +x libp2p_node
  ```
  Make sure you satisfy the <a href="../quickstart">system requirements</a>.
- or within a docker image using the provided Dockerfile:
  ``` bash
  docker build -t acn_node_standalone -f scripts/acn/Dockerfile .
  ```

Next, to run the node binary in standalone mode, it requires values for the following entries:

- `AEA_P2P_ID`: the node's private key, will be used as its identity
- `AEA_P2P_URI`: the local host and port to use by node
- `AEA_P2P_URI_PUBLIC`: the URI under which the peer is publicly reachable
- `AEA_P2P_DELEGATE_URI`: the URI under which the peer receives delegate connections
- `AEA_P2P_ENTRY_URIS`: an optionally supplied list of comma-separated (`,`) entry <a href="https://multiformats.io/multiaddr/" target="_blank">Multiaddrs</a> for the peer to bootstrap 

The script allows different methods to pass these values to the node:

- As environment variables exported in the format `<ENTRY_KEYWORD>=<ENTRY_VALUE>` for each entry. Then:
  ``` bash
  python3 run_acn_node_standalone.py libp2p_node --config-from-env
  ```
- Using an environment file containing the entries and their values in the format `<ENTRY_KEYWORD>=<ENTRY_VALUE>`, one entry per line. Then:
  ``` bash
  python3 run_acn_node_standalone.py libp2p_node --config-from-file <env-file-path>
  ```
  or
  ``` bash
  docker run -v <acn_config_file>:/acn/acn_config -it acn_node_standalone --config-from-file /acn/acn_config
  ```
- Using command line arguments:
  ``` bash
  python3 run_acn_node_standalone.py libp2p_node --key-file <node_private_key.txt> \
    --uri <AEA_P2P_URI> --uri-external <AEA_P2P_URI_PUBLIC>  \
    --uri-delegate <AEA_P2P_DELEGATE_URI> \
    --entry-peers-maddrs <AEA_P2P_ENTRY_URI_1> <AEA_P2P_ENTRY_URI_2> ...
  ```
  or 
  ``` bash
  docker run -v <node_private_key.txt>:/acn/key.txt -it acn_node_standalone --key-file /acn/key.txt \
    --uri <AEA_P2P_URI> --uri-external <AEA_P2P_URI_PUBLIC>  \
    --uri-delegate <AEA_P2P_DELEGATE_URI> \
    --entry-peers-maddrs <AEA_P2P_ENTRY_URI_1> <AEA_P2P_ENTRY_URI_2> ...
  ```

Note that the script will always save the configuration of the running node as a file under the name `.acn_config` in the current working directory. This can be handy when you want the exact same configuration for future runs of the node.