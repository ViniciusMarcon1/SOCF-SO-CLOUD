import os
import platform
import psutil
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/info")
def info():
    return "Nomes: Gustavo Muniz e Vinicius Marcon"

@app.route("/metrica")
def metrica(): 
    pid = os.getpid()
    processo = psutil.Process(pid)
    memoria = processo.memory_info().rss / (1024 * 1024)
    cpu = processo.cpu_percent(interval=0.1)
    so_nome = platform.system()
    so_versao = platform.release()

    dados = {
        "PID": pid, 
        "Memória Usada": round(memoria, 2), 
        "% CPU": round(cpu, 2), 
        "Sistema Operacional": f"{so_nome} ({so_versao})"
    }

    return jsonify(dados)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)