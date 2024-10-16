def Open(file_name, mode):
    try:
        file = open(file_name, mode, encoding='utf-8')
    except Exception as e:
        print("File", file_name, "wasn't opened!", e)
        return None
    else:
        print("File", file_name, "was opened!")
        return file


def create_file_tf8_1(file_name):
    lines = [
        "The flight number 1717 is postponed for 40 minute, the boarding will start at 5 a.m.",
    ]
    file = Open(file_name, "w")
    if file is not None:
        for line in lines:
            file.write(line + '\n')
        file.close()
        print(f"Information was successfully added to {file_name}!")

def process_file_tf8_1_to_tf8_2(input_file_name, output_file_name):
    file_2_r = Open(input_file_name, "r")
    file_2_w = Open(output_file_name, "w")
    
    if file_2_r is not None and file_2_w is not None:
        content = file_2_r.read()
        current_line = ""
        processed_lines = []
        
        for char in content:
            if char.isdigit():
                continue  
            current_line += char
            if len(current_line) == 10:
                processed_lines.append(current_line)
                current_line = ""
       
        if current_line:
            processed_lines.append(current_line)
       
        for index, line in enumerate(processed_lines, start=1):
            file_2_w.write(f"{index:5} {line}\n")
        
        file_2_r.close()
        file_2_w.close()
        print("Files were closed!")

def read_file_tf8_2(file_name):
    file_3_r = Open(file_name, "r")
    if file_3_r is not None:
        for line in file_3_r:
            print(line, end='')
        file_3_r.close()
        print(f"File {file_name} was closed!")

file1_name = "TF8_1.txt"
file2_name = "TF8_2.txt"

create_file_tf8_1(file1_name)
process_file_tf8_1_to_tf8_2(file1_name, file2_name)
print("New sequence:")
read_file_tf8_2(file2_name)