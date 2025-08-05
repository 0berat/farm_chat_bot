#!/bin/bash

python3 chunking_process/extract_text.py

sudo docker-compose up -d

source /mnt/ikinci_disk/proje_tarim/venv/bin/activate

python3 chunking_process/index_to_weaviate.py

cd tarim-chat-ui
npm run dev &
cd ..

uvicorn main:app --reload
