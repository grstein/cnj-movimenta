#!/bin/bash

docker run -it -p 8050:8050 -v /home/stein/Estudos/'Ciência de Dados'/datascience/cnj-inova/app:/web --entrypoint python plotly:tst /web/app.py
