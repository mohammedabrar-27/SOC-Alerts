with open(r"C:\Users\Samsung\Downloads\soc_files\soc_files\log_files\Security.log") as f:
    logs = f.readlines()

deleted_accounts = [line for line in logs if "4726" in line]
print(f"Accounts deleted detected: {len(deleted_accounts)}")
