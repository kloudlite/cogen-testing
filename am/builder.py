import yaml
import os
import importlib

# Check if the .am folder exists
am_folder_path = 'working/.am'
if not os.path.exists(am_folder_path):
  raise FileNotFoundError(f"The folder '{am_folder_path}' does not exist.")

# Specify the path to your YAML files
tools_yaml_file_path = os.path.join(am_folder_path, 'tools.yaml')
if not os.path.exists(tools_yaml_file_path):
  tools_yaml_file_path = os.path.join(am_folder_path, 'tools.yml')

agents_yaml_file_path = os.path.join(am_folder_path, 'agents.yaml')
if not os.path.exists(agents_yaml_file_path):
  agents_yaml_file_path = os.path.join(am_folder_path, 'agents.yml')

# Open the YAML files and load their content
with open(tools_yaml_file_path, 'r') as tools_file:
  tools_list = yaml.safe_load(tools_file)

with open(agents_yaml_file_path, 'r') as agents_file:
  agents_list = yaml.safe_load(agents_file)

# Transform lists into dictionaries with names as keys
tools = {item['name']: item for item in tools_list}
agents = {item['name']: item for item in agents_list}

# Now `tools` and `agents` contain the parsed YAML content as Python dictionaries
# print(tools)
# print(agents)

for tool_name, tool_info in tools.items():
  # module_name, class_name = tool_info['tool'].rsplit('.', 1)
  # module = importlib.import_module(module_name)
  # tool_class = getattr(module, class_name)
  # Change directory to the parent directory
  # parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
  # os.chdir(parent_dir)

  # Run docker build command
  os.system(f'docker build -f am/run-tool/Dockerfile --build-arg TOOL_NAME={tool_name} -t img_{tool_name.lower()} .')
  # build tool 
  # print(f"Loaded tool: {tool_name} -> {tool_class.__kl__name__}")

