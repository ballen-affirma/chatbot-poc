import json
import random

data = []

with open("embeddings_dataset_corpus.jsonl", "r") as corpus:
    for line in corpus.readlines():
        if "https://alorica.com/careers/" in line:
            continue
        data.append(json.loads(line))

print("Read", len(data), "lines.")

queries_data = []
mappings_data = []

for i in range(100):
    print("=====", i, "=====")
    idx = random.randint(0, len(data)-1)
    title = data[idx]['title']
    text = data[idx]['text']
    print("Title:", title)
    print("Text:", text)

    id = "query" + str(i)
    query = input("Query: ").strip()
    if query == "":
        print("Early exit")
        break
    else:
        queries_data.append({"_id": id, "query": query})
        mappings_data.append({"query-id": id, "corpus-id": data[idx]["_id"], "score": "1"})
    print("\n")

prefix = input("Give a prefix for these files: ")

with open(prefix + "_dataset_queries.jsonl", "w") as queries_file:
    for q in queries_data:
        queries_file.write(json.dumps(q))
        queries_file.write("\n")

random.shuffle(mappings_data)
train_count = int(0.8 * len(mappings_data))
train_data = mappings_data[:train_count]
test_data = mappings_data[train_count:]

with open(prefix + "_dataset_train.tsv", "w") as train_file:
    train_file.write("query-id\tcorpus-id\tscore\n")
    for d in train_data:
        train_file.write(d['query-id']+"\t"+d['corpus-id']+"\t"+d['score']+"\n")

with open(prefix + "_dataset_test.tsv", "w") as test_file:
    test_file.write("query-id\tcorpus-id\tscore\n")
    for d in test_data:
        test_file.write(d['query-id']+"\t"+d['corpus-id']+"\t"+d['score']+"\n")
