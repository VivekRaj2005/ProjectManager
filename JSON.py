import shutil
import os
from json import loads


class JSONWriter:
    def __init__(self, fname):
        self.file_name = fname

    def WriteToFile(self, content):
        Qutes = False
        number = 0
        str_content = str(content)
        fin_content = ""
        for char in str_content:
            if char == "{":
                if not Qutes:
                    number += 1
                    fin_content += "{\n"
                    for _ in range(number):
                        fin_content += "\t"
                else:
                    fin_content += char

            elif char == ",":
                if not Qutes:
                    fin_content += ",\n"
                    for _ in range(number):
                        fin_content += "\t"
                else:
                    fin_content += char

            elif char == "'":
                if not Qutes:
                    fin_content += "\""
                    Qutes = True
                else:
                    fin_content += "\""
                    Qutes = False
            elif char == "\"":
                if not Qutes:
                    fin_content += "\""
                    Qutes = True
                else:
                    fin_content += "\""
                    Qutes = False
            elif char == "}":
                if not Qutes:
                    fin_content += "\n"
                    number -= 1
                    for _ in range(number):
                        fin_content += "\t"
                    fin_content += "}"
                else:
                    fin_content += char
            elif char == "[":
                if not Qutes:
                    fin_content += "\n"
                    for _ in range(number):
                        fin_content += "\t"
                    fin_content += "["
                    fin_content += "\n"
                    number += 1
                    for _ in range(number):
                        fin_content += "\t"
                else:
                    fin_content += char

            elif char == "]":
                if not Qutes:
                    fin_content += "\n"
                    number -= 1
                    for _ in range(number):
                        fin_content += "\t"
                    fin_content += "]"
                else:
                    fin_content += char

            elif char == " ":
                if not Qutes:
                    fin_content += ""
                else:
                    fin_content += char

            else:
                fin_content += char
        fin_content += "\n"
        if os.path.exists(f"{self.file_name}.json"):
            os.remove(f"{self.file_name}.json")
        if os.path.exists(f"{self.file_name}.txt"):
            os.remove(f"{self.file_name}.txt")
        with open(f"{self.file_name}.txt", "a") as file:
            file.write(fin_content)
        shutil.move(f"{self.file_name}.txt", f"{self.file_name}.json")

    def ReadFromFile(self) -> {}:
        lines = []
        final_lines = []
        return_string = ""
        shutil.move(f"{self.file_name}.json", f"{self.file_name}.txt")
        str_response = ""
        flag = False
        with open(f"{self.file_name}.txt", "r") as file:
            while not flag:
                str_response = file.readline()
                if str_response == "":
                    flag = True
                else:
                    lines.append(str_response)
        shutil.move(f"{self.file_name}.txt", f"{self.file_name}.json")
        for line in lines:
            final_line = ""
            for char in line:
                if char == "\n":
                    final_line += ""
                elif char == "\t":
                    final_line += ""
                else:
                    final_line += char
            final_lines.append(final_line)
        for final_line in final_lines:
            return_string += final_line

        return loads(return_string)
