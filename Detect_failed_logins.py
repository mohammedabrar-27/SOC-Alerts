with open(r"C:\Users\Samsung\Downloads\soc_files\soc_files\log_files\Security.log") as f:
    logs = f.readlines()

failed_logins = [line for line in logs if "4625" in line]
print(f"Failed logins detected: {len(failed_logins)}")
