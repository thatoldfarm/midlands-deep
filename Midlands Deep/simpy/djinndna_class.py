import re
import ast
import json

class CodeParser:
    def __init__(self, file_path, output_path):
        self.file_path = file_path
        self.output_path = output_path

    def read_and_clean_file(self):
        with open(self.file_path, 'r') as file:
            return file.read()

    def parse_node(self, node, code_lines):
        start_line = node.lineno - 1
        end_line = node.end_lineno
        node_lines = code_lines[start_line:end_line]
        body = "\n".join(node_lines)

        if isinstance(node, ast.FunctionDef):
            return {
                'type': 'function',
                'name': node.name,
                'parameters': [param.arg for param in node.args.args],
                'body': body
            }
        elif isinstance(node, ast.ClassDef):
            methods = []
            for item in node.body:
                if isinstance(item, ast.FunctionDef):
                    m_lines = code_lines[item.lineno - 1:item.end_lineno]
                    methods.append({
                        'type': 'function',
                        'name': item.name,
                        'parameters': [param.arg for param in item.args.args],
                        'body': "\n".join(m_lines)
                    })
            return {
                'type': 'class',
                'name': node.name,
                'methods': methods,
                'body': body
            }
        else:
            return {
                'type': 'raw',
                'body': body
            }

    def parse_code_structure(self, code):
        code_lines = code.split("\n")
        parsed_ast = ast.parse(code)
        return [self.parse_node(node, code_lines) for node in ast.iter_child_nodes(parsed_ast) if node is not None]

    def write_to_json_file(self, structure):
        with open(self.output_path, 'w') as file:
            json.dump(structure, file, indent=4)

    def parse_and_write_structure(self):
        cleaned_code = self.read_and_clean_file()
        rna_dna_structure_parsed_all = self.parse_code_structure(cleaned_code)
        self.write_to_json_file(rna_dna_structure_parsed_all)

if __name__ == "__main__":
    file_path = 'sim.py'  # Path to sim.py
    rna_dna_structure_path = 'rna_dna_structure.json'  # Output JSON file path

    parser = CodeParser(file_path, rna_dna_structure_path)
    parser.parse_and_write_structure()
