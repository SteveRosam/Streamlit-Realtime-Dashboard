```mermaid
%%{ init: { 'flowchart': { 'curve': 'monotoneX' } } }%%
graph LR;
Demo_Data_Source[Demo Data Source] -->|f1-data|Streamlit_Dashboard[Streamlit Dashboard];
Demo_Data_Source[Demo Data Source] -->|f1-data|influxdb-3-destination[influxdb-3-destination];

```