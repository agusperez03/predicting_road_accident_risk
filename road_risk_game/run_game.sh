#!/bin/bash

echo "===================================="
echo " ROAD RISK GAME - QUICK START"
echo "===================================="
echo ""
echo "Iniciando juego..."
echo ""

cd "$(dirname "$0")"
streamlit run app.py
