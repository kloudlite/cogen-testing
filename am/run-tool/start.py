import yaml
import os
import sys
import importlib.util
from tool import ToolRunner

cwd = os.getcwd()
if cwd not in sys.path:
  sys.path.append(cwd)

# Check if the .am folder exists
am_folder_path = 'working/.am'
if not os.path.exists(am_folder_path):
  raise FileNotFoundError(f"The folder '{am_folder_path}' does not exist.")

# Specify the path to your YAML files
tools_yaml_file_path = os.path.join(am_folder_path, 'tools.yaml')
if not os.path.exists(tools_yaml_file_path):
  tools_yaml_file_path = os.path.join(am_folder_path, 'tools.yml')

# Open the YAML files and load their content
with open(tools_yaml_file_path, 'r') as tools_file:
  tools_list = yaml.safe_load(tools_file)

# Transform lists into dictionaries with names as keys
tools = {item['name']: item for item in tools_list}


# Now `tools` contains the parsed YAML content as Python dictionaries
tool_name = os.getenv('TOOL_NAME', 'GmailTool')
tool_info = tools[tool_name]
module_name, class_name = tool_info['tool'].rsplit('.', 1)

module_name = f"working.{module_name}"

# print(module_name, class_name)

spec = importlib.util.find_spec(module_name)
if spec is None:
  raise ImportError(f"Module '{module_name}' not found.")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
tool_class = getattr(module, class_name)

toolRunner = ToolRunner(tool_class)
toolRunner.run()
