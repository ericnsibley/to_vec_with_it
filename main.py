import weaviate
import json
import os 

def main(): 
    client = weaviate.Client("http://localhost:8080")

    print(os.getcwd())


    with open('./schema.json') as schemaFile:
        schema = json.load(schemaFile)
    
    # split up migration into different script? 
    # or at least add try / catch
    # client.schema.create(schema) 

    # client.batch(
    #     batch_size=100,
    #     dynamic=True,
    #     num_workers=4
    # )

    print(client.schema.get())


if __name__ == '__main__':
    main()