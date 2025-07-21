#!/bin/bash

echo "📦 Checking for Ollama..."
if ! command -v ollama &> /dev/null
then
    echo "🔧 Installing Ollama..."
    curl -fsSL https://ollama.com/install.sh | sh
else
    echo "✅ Ollama already installed."
fi

echo "🧠 Pulling LLaMA 3 model..."
ollama pull llama3

echo "✅ Setup complete. Run with: python dat_llm.py"
