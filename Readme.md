# Excel Data Entry Forms Manager App

An open source PyQt5 application for creating, editing, and managing Excel data entry forms.

## User Flow

![User Flow](assets/USer%20flow.png)

### Create Form

![Create Form](assets/Create%20Form.png)

### Data Entry Form

![Data Entry Form](assets/Data%20Entry%20Form.png)

# Running the App

You can use either **pip** or **uv** to manage dependencies.

### Option 1: Using uv (recommended)

1. Create a virtual environment:
   ```sh
   uv venv
   ```
2. Install dependencies:
   ```sh
   uv pip install -r requirements.txt
   ```
3. Run the app:
   ```sh
   python main.py
   ```

### Option 2: Using pip

1. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
2. Activate the virtual environment:
   - On Windows:
     ```sh
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Run the app:
   ```sh
   python main.py
   ```

## License

MIT License
