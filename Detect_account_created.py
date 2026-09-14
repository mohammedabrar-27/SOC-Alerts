with open(r"C:\Users\Samsung\Downloads\soc_files\soc_files\log_files\Security.log") as f:
    logs = f.readlines()

created_accounts = [line for line in logs if "4720" in line]
print(f"Accounts created detected: {len(created_accounts)}")