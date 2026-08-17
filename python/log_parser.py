from pathlib import Path
import sys

def log_parser(file_name: str):
    if len(sys.argv) > 1 :
        file_name = Path(sys.argv[1])
    file_path = f"{Path(__file__).parent}/{file_name}"
    errors_in_file = []
    unique_errors_in_file = set()
    with open(file_path, "r") as log_file_to_parse:
        info, error, warning = 0, 0, 0
        while line := log_file_to_parse.readline():
            parts = line.split()
            if 'INFO' == parts[2]:
                info += 1
            elif 'WARNING' == parts[2]:
                warning += 1
            elif 'ERROR' == parts[2]:
                error += 1
                errors_in_file.append(line)
                unique_errors_in_file.add(' '.join(parts[3:]))
    print('INFO    :', info)
    print('WARNING :', warning)
    print('ERROR   :', error)
    print('TOTAL   :', (info + warning + error))
    for element in errors_in_file:
        print(element)
    if len(errors_in_file) > 0:
        print("The first Error in log is        :",errors_in_file[0])
    else:
        print("No Error in log")
    print ("These are unique errors in file     :",unique_errors_in_file)
log_parser("application.log")
