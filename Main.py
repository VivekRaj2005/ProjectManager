#!/usr/bin/env python3

from Config import Project_Data, Output_Data, Terminal
from os.path import exists
from os import getcwd, listdir, mkdir, system
from JSON import JSONWriter
from sys import argv

if __name__ == "__main__":
    if not exists(f"{Project_Data}.json"):
        Data = [
                {
                    "Project Name": "Project Manager",
                    "Path" : getcwd(),
                    "Language": "Python"
                }
            ]
        JSONWriter(Project_Data).WriteToFile(Data)

    if len(argv) > 1:
        if argv[-1] == "--add":
            def_name = getcwd()[str(getcwd()).rindex("/") + 1:]
            project_name = input(f"Project Name ({def_name}):")
            if project_name == "":
                project_name = def_name
            def_path = getcwd()
            project_path = input(f"Project Path: ({def_path}):")
            if project_path == "":
                project_path = def_path
            project_lang = input("Project Language (Python):")
            if project_lang == "":
                project_lang = "Python"
            new_data = {
                "Project Name": project_name,
                "Path": project_path,
                "Language": project_lang
            }
            list_ = list(JSONWriter(Project_Data).ReadFromFile())
            list_.append(new_data)
            JSONWriter(Project_Data).WriteToFile(list_)

        elif argv[-1] == "--update":
            Data = JSONWriter(Project_Data).ReadFromFile()
            Menu_Data = []
            for project in Data:
                data = {}
                data["name"] = f"\t{project['Project Name']}"
                data["command"] = f"{Terminal} devour emacsclient -c {project['Path']} &"
                if project["Language"] == "Python":
                    data['icon'] = "python"
                elif project["Language"] == "C++" or project["Language"] == "C":
                    data['icon'] = "text-x-c++src"
                elif project["Language"] == "Bash":
                    data['icon'] = "bash"
                elif project["Language"] == "Config":
                    data['icon'] = "computersettings"
                else:
                    data['icon'] = "accessories-text-editor"
                Menu_Data.append(data)

            JSONWriter(Output_Data).WriteToFile(Menu_Data)

