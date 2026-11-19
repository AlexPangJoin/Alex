log_file = None
try:
    log_file = open("log.txt","w")
    log_file.write("Application started.\n")
    log_file.write("User 'admin' logged in.\n")

except IOError as e:
    print(f"Error writing initial log: {e}")
finally:
    if log_file is not None and not log_file.closed:
        log_file.close()

log_file = None
try:
    log_file = open("log.txt", "a")
    log_file.write("Action: Data saved.\n")
    log_file.write("Application shut down.\n")
    print("Log entries successfully written to log.txt")

except IOError as e:
    print(f"Error appending to log file: {e}")
finally:
    if log_file is not None and not log_file.closed:
        log_file.close()