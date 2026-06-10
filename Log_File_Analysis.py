#Read log file
err = 0
warnin = 0
latest_err = None
with open("sample_log.txt","r") as f:
    logs = f.readlines()
    

    for line in logs:
        if "ERROR" in line:
            err +=1
            latest_err = line.strip()

        elif "WARNING" in line:
            warnin +=1


print("Log File Analysis Summary")
print("Error Count:",err)
print("Warning count:",warnin)

if latest_err:
    print("Latest error:",latest_err)
else:
    print("No error found")
    


