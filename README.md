# 🍃 MotivZen v1.0

> **An automated Python agent for real-time quote fetching and local archival.**

---

### 🚀 Overview
**MotivZen** is my first "Build in Public" project. It’s a minimalist CLI (Command Line Interface) tool that interfaces with the ZenQuotes REST API to fetch inspiration and handle automated file persistence with precise timestamps.

### 🛠️ Tech Stack
- **Language:** Python 3.10+
- **API:** [ZenQuotes.io](https://zenquotes.io/)
- **Libraries:** - `requests`: Handling HTTP protocols and API responses.
  - `os`: Managing dynamic directory creation and file paths.
  - `datetime`: Implementing granular timestamping for data versioning.

### ⚡ Features
- **Remote Integration:** Real-time GET requests to external cloud providers.
- **Automated Persistence:** Dynamic system folder creation and UTF-8 file writing.
- **Smart Cataloging:** Files are automatically named using a `DD-MM-YYYY_HHMMSS` schema to prevent data collisions.
- **Clean CLI Interface:** Interactive user loop for seamless operation.

### 📂 Installation & Setup
```bash
# 1. Clone the repository
git clone [https://github.com/AbdoulayeSowX/MotivZen.git](https://github.com/AbdoulayeSowX/MotivZen.git)

# 2. Enter the directory
cd MotivZen

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the agent
python citationsGenerator.py