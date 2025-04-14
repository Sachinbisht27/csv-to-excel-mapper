# 📊 CSV to Excel Mapper

A simple Python utility that reads data from a CSV file and maps it into a predefined Excel template. Useful for automating repetitive Excel data entry tasks using a structured CSV input.

---

## 🚀 Features

- Reads data from a CSV file
- Maps CSV columns to specific Excel columns
- Writes data into an Excel template starting from a specified row
- Preserves Excel formatting and headers

---

## 🧰 Requirements

- Python 3.7+
- pip (Python package manager)

---

## 🧪 Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Sachinbisht27/csv-to-excel-mapper.git
    ```

2. Switch to project folder and setup the virtual environment:
    ```bash 
    cd csv-to-excel-mapper
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    ```bash
    source ./venv/bin/activate
    ```

4. Install the dependencies:
   ```sh
   pip3 install -r requirements.txt
   ```

5. Run the script using `python script.py`

## 📌 Notes:

- The script assumes headers are already present in the Excel template (row 1).
- Writing begins from row 2.
- Uses openpyxl, so Excel styles and formatting are preserved.

## 📃 License
MIT License. Feel free to use, modify, and distribute.
