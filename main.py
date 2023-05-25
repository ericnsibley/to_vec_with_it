import weaviate
import json
import download


def create_schema_from_file(client, file: str) -> None:
    with open(file) as schemaFile:
        schema = json.load(schemaFile)
    
    try: 
        client.schema.create(schema) 
    except weaviate.exceptions.UnexpectedStatusCodeException as e:
        print("The new schema has a conflict with what is already in the database: ", e.message, '\n') 
    # print(client.schema.get())


def upload_to_db(client, topic: str) -> None:
    article_data = download.download_articles_related_to(topic, 10)

    with client.batch as batch: 
        batch.batch_size = 100
        for i, data in enumerate(article_data):
            print(f"importing article data {i + 1}")
            batch.add_data_object(data, "Article")


# could use some variable field fetching + selection validation, but this is a first pass
def fetch_from_db(client, concepts: list[str]):
    nearText = {"concepts": concepts} 
    result = (
        client.query.get("Article", ["title", "authors", "date_published", "summary", "pdf_url"])
        .with_near_text(nearText)
        .with_limit(1)
        .do()
    )
    return result


def main(): 
    client = weaviate.Client("http://localhost:8080")

    create_schema_from_file(client, './article_schema.json')    

    upload_to_db(client, "electrons")

    result = fetch_from_db(client, ["heat"]) # the current second article talks about electron thermodynamics
    print(json.dumps(result,indent=4))


if __name__ == '__main__':
    main()