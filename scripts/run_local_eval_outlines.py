import sys
sys.path.append('..')

import json
from pathlib import Path

from eval.config import ROOT_DIR, BATCH_SIZE
from eval.local import generate

# Load original dataset
with open(Path(ROOT_DIR, "data/processed/gorilla_openfunctions_v1_test_simple_jsonschema.jsonl"), "r") as f:
    data = [json.loads(item) for item in list(f)[0:10]]

with open(Path(ROOT_DIR, "data/results/gorilla_openfunctions_v1_test_simple_outlines.jsonl"), "w") as f:
    for i in range(0, len(data), BATCH_SIZE):
        questions = [item["question"] for item in data[i:i+BATCH_SIZE]]
        schemas = [item["schema"] for item in data[i:i+BATCH_SIZE]]
        for question, schema in zip(questions, schemas):
            function_call = generate(question, schema)
            f.write(json.dumps(function_call) + "\n")