import os
import signal
from multiprocessing import Process
from flask import Flask, request, render_template_string


def create_app(server_id):
    app = Flask(__name__)

    @app.route('/')
    def home():
        return render_template_string(
            """
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Server {{ server_id }}</title>
                <style>
                    body {
                        font-family: Arial, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                        background-color: #f0f0f0;
                    }
                    .container {
                        text-align: center;
                        padding: 50px;
                        background-color: white;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                    }
                    h1 {
                        color: #333;
                    }
                    p {
                        color: #666;
                    }
                    button {
                        padding: 10px 20px;
                        font-size: 16px;
                        color: white;
                        background-color: #007BFF;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                    }
                    button:hover {
                        background-color: #0056b3;
                    }
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>Welcome to Server {{ server_id }}</h1>
                    <p>This is server number {{ server_id }}</p>
                    <button onclick="showAlert()">Click Me</button>
                    <button onclick="refreshPage()">Refresh</button>
                </div>
                <script>
                    function showAlert() {
                        alert('You are on server {{ server_id }}');
                    }
                    function refreshPage() {
                        location.reload();
                    }
                </script>
            </body>
            </html>
            """, server_id=server_id)

    return app


def run_server(server_id):
    app = create_app(server_id)
    port = 5000 + int(server_id)
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    num_servers = 5  # Number of servers you want to run
    processes = []

    def terminate_processes(signum, frame):
        for process in processes:
            process.terminate()
        for process in processes:
            process.join()
        exit(0)
    signal.signal(signal.SIGINT, terminate_processes)

    for i in range(num_servers):
        server_id = str(i + 1)
        process = Process(target=run_server, args=(server_id,))
        process.start()
        processes.append(process)

    for process in processes:
        process.join()
