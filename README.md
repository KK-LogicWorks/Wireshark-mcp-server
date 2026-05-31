\# PCAP MCP Server



An MCP (Model Context Protocol) server for Wireshark/TShark packet analysis, live network capture, and AI-assisted network investigations.



\## Features



\* Protocol discovery from PCAP files

\* Packet filtering using Wireshark display filters

\* TCP/UDP stream analysis

\* Network conversation analysis

\* Traffic statistics

\* Live packet capture

\* Interface discovery

\* MCP STDIO transport

\* MCP HTTP transport



\## Architecture



```text

AI Client

&#x20;   |

&#x20;   v

PCAP MCP Server

&#x20;   |

&#x20;   +-- TShark

&#x20;   +-- Wireshark Engine

&#x20;   |

&#x20;   +-- PCAP Files

&#x20;   +-- Live Network Interfaces

```



\## Requirements



\* Python 3.11+

\* Wireshark

\* TShark



Verify installation:



```bash

tshark -v

```



\## Installation



```bash

git clone https://github.com/<your-username>/pcap-mcp-server.git



cd pcap-mcp-server



python -m venv venv



venv\\Scripts\\activate



pip install -r requirements.txt

```



\## Configuration



Create a `.env` file:



```env

TSHARK\_PATH=C:\\\\Program Files\\\\Wireshark\\\\tshark.exe

MAX\_TIMEOUT=30

MAX\_PACKETS=10000

HTTP\_HOST=0.0.0.0

HTTP\_PORT=8080

```



\## Run



STDIO transport:



```bash

python run.py --transport stdio

```



HTTP transport:



```bash

python run.py --transport http

```



\## Available Modules



\### Discovery



\* Protocol discovery



\### Packets



\* Packet search

\* Packet filtering



\### Conversations



\* Network conversation analysis



\### Streams



\* TCP/UDP stream inspection



\### Statistics



\* Traffic statistics



\### Live Capture



\* Live packet capture



\### Interfaces



\* Network interface enumeration



\### Behavior



\* Network behavior analysis



\## Project Structure



```text

app/

├── tools/

├── transports/

├── prompts/

├── resources/

├── utils/

├── config.py

└── server.py



run.py

requirements.txt

```



\## License



MIT License



