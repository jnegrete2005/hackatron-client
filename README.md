# 🤖 HackaTron Client Example

This repository provides a **template bot client** for the [HackaTron](https://github.com/jnegrete2005/hackatron) AI competition.  
You can build your own bot in **Python** 🐍 or any other language of your choice!

---

## 🚀 Getting Started

### 1️⃣ Clone the repo

```bash
git clone git@github.com:jnegrete2005/hackatron-client.git
cd hackatron-client
```

### 2️⃣ Install the required dependencies (if developing in Python):

```bash
pip install -r requirements.txt
```

---

## 🧠 Developing Your Bot

You'll find a simple example bot in the `src/example.py` file. This bot makes random moves in the Tron game. You can modify this file to implement your own bot logic.

Your bot should:

- Read the game state from standard input (stdin).
- Decide the next move based on the game state.
- Output the chosen move to standard output (stdout).

You can customize the logic however you like — ML models, heuristics, pathfinding, etc. 🧩

---

## 🐳 How to test your bot locally

Your client includes a [Dockerfile](./Dockerfile).
This has a template to launch a container (runned in Python) that will be excecuted by the server so your bot plays.

This Dockerfile generates a Docker Image with the command:

```bash
docker build -t <DOCKER_USERNAME>/<YOUR_IMAGE_NAME> .
```

The HackaTron team has also provided a very simple bot, a random bot, in [Docker Hub](https://hub.docker.com/r/jokkess/hackatron-random-bot). You can use this image to test your bot against it.

To run a local server and test your bot against the random bot, go to the HackaTron server repository and follow the instructions in the [README.md](https://github.com/jokkess/hackatron) file.

---

## 📝 How to submit your bot

To submit your bot to the HackaTron competition, you need to push your Docker image to Docker Hub so the HackaTron server can pull it and run it.

### 1️⃣ Log in to your Docker Hub account:

```bash
docker login
```

### 2️⃣ Build your Docker image (if you haven't already):

```bash
docker build -t <DOCKER_USERNAME>/<YOUR_IMAGE_NAME> .
```

### 3️⃣ Push your Docker image to Docker Hub:

```bash
docker push <DOCKER_USERNAME>/<YOUR_IMAGE_NAME>
```

### 4️⃣ Submit your bot to the HackaTron competition

Once your image is pushed, you can submit it to the HackaTron competition by providing the image name to the HackaTron submission system.  
Make sure to follow any additional submission guidelines provided by the HackaTron team.

---

## 🏆 Good luck, and may the best bot win!

Made with ❤️ by the HackaTron Team
