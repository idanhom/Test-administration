from openpyxl import load_workbook

def update_excel_file(excel_file_path, first_name, last_name, email):
    try:
        wb = load_workbook(excel_file_path)
    except FileNotFoundError:
        print(f"Error: Excel file not found at {excel_file_path}")
        sys.exit(1)
    ws = wb.active
    ws.append([first_name, last_name, email])
    wb.save(excel_file_path)
