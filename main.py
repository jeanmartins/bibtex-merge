import os

path = "C:/bibtex"

if not os.path.exists(path):
    print(f"O caminho {path} não existe.")
else:

    files = [f for f in os.listdir(path) if f.endswith(".bib")]

    if not files:
        print("Nenhum arquivo .bib foi encontrado.")
    else:
        print(f"Arquivos .bib encontrados: {files}")

        merged = []

        for file in files:
            file_path = os.path.join(path, file)
            print(f"Lendo o arquivo: {file_path}")
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                if content: 
                    merged.append(content)
                else:
                    print(f"O arquivo {file_path} está vazio.")

        if not merged:
            print("Nenhum dado foi lido dos arquivos.")
        else:
            combined_data = "\n".join(merged)

            output_file_path = os.path.join(path, "merged.bib")
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                output_file.write(combined_data)

            print(f"Novo arquivo 'merged.bib' criado com sucesso no caminho: {output_file_path}")
