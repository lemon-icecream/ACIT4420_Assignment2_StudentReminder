## 🧰 Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
```

### 2. Create a Virtual Environment
```bash
cd src
python3 -m venv testenv
source testenv/bin/activate  
```
On Windows, use `testenv\Scripts\activate`

### 3. Install the Package
```bash
pip install -e .
```

### 4. Run
Runs the scheduler to send reminders at each student’s preferred time.
```bash
study-reminders
```
Sends all reminders immediately (useful for debugging or demos).
```bash
study-reminders --test
```

### 5. Deactivate the Environment
When done, deactivate it with:
```bash
deactivate
```
