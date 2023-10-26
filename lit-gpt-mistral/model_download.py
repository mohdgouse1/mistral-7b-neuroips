from huggingface_hub import snapshot_download

snapshot_download(
    repo_id="preetlalli/mistral-7B-deepspeed",
    token="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",
    local_dir="mistral-7b-deepseed",
)
