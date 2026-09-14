with open(r"C:\Users\Samsung\Downloads\soc_files\soc_files\log_files\Security.log") as f:
    logs = f.readlines()

disabled_accounts = [line for line in logs if "4725" in line]
print(f"Accounts disabled detected: {len(disabled_accounts)}")
